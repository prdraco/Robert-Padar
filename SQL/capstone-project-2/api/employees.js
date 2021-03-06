const express = require('express');
const employeesRouter = express.Router();
const timesheetsRouter = require('./timesheets.js');
const sqlite3 = require('sqlite3');
const db = new sqlite3.Database(process.env.TEST_DATABASE || './database.sqlite');

/*/api/employees/:employeeId
GET
Returns a 200 response containing the employee with the supplied employee ID on 
the employee property of the response body
If an employee with the supplied employee ID doesn’t exist, returns a 404 response*/
employeesRouter.param('employeeId', (req, res, next, employeeId) => {
    const sql = `SELECT * FROM Employee WHERE Employee.id = $employeeId`;
    const values = {$employeeId: employeeId};
    db.get(sql, values, (error, employee) => {
        if(error) {
            next(error);
        } else if(employee) {
            req.employee = employee;
            next();
        } else {
            res.sendStatus(404);
        }
    });
});

employeesRouter.use('./:employeeId/timesheets', timesheetsRouter);

/* GET
Returns a 200 response containing all saved currently-employed employees 
(is_current_employee is equal to 1) on the employees property of the 
response body*/
employeesRouter.get('/', (req, res, next) => {
    db.all(`SELECT * FROM Employee WHERE Employee.is_current_employee = 1`,
    (error, employees) => {
        if(error) {
            next(error);
        } else {
            res.status(200).json({ employees: employees});
        }
    });
});

employeesRouter.get('/:employeeId', (req, res, next) => {
    res.status(200).json({ employee: req.employee });
});

/*POST
Creates a new employee with the information from the employee property of 
the request body and saves it to the database. Returns a 201 response with 
the newly-created employee on the employee property of the response body
If any required fields are missing, returns a 400 response*/
employeesRouter.post('/', (req, res, next) => {
    const name = req.body.employee.name;
    const position = req.body.employee.position;
    const wage = req.body.employee.wage;
    const isCurrentEmployee = req.body.employee.isCurrentEmployee === 0 ? 0 : 1;
    if(!name || !position || !wage) {
        return res.sendStatus(400);
    }
    const sql = `INSERT INTO Employee (name, position, wage, is_current_employee)
    VALUES ($name, $position, $wage $isCurrentEmployee)`;
    const values = {
        $name: name,
        $position: position,
        $wage: wage,
        $isCurrentEmployee: isCurrentEmployee
    };
    db.run(sql, values, (error) => {
        if(error) {
            next(error);
        } else {
            db.get(`SELECT * FROM Employee WHERE Employee.id = ${this.lastID}`,
            (error, employee) => {
               res.sendStatus(201).json({ employee: employee }); 
            });            
        }
    });
});

/*PUT
Updates the employee with the specified employee ID using the information from 
the employee property of the request body and saves it to the database. 
Returns a 200 response with the updated employee on the employee property of 
the response body
If any required fields are missing, returns a 400 response
If an employee with the supplied employee ID doesn’t exist, returns a 404 response*/
employeesRouter.put('./:employeeId', (req, res, next) => {
    const name = req.body.employee.name;
    const position = req.body.employee.position;
    const wage = req.body.employee.wage;
    const isCurrentEmployee = req.body.employee.isCurrentEmployee === 0 ? 0 : 1;
    if(!name || !position || !wage) {
        return res.sendStatus(400);
    }
    const sql = `UPDATE Employee SET name = $name, position = $position, wage = $wage,
    is_current_employee = $isCurrentEmployee WHERE Employee.id = $employeeId`;
    const value = {
        $name: name,
        $position: position,
        $wage: wage,
        $isCurrentEmployee: isCurrentEmployee,
        $employeeId: req.params.employeeId
    };
    db.run(sql, value, (error) => {
        if(error) {
            next(error);
        } else {
            db.get(`SELECT * FROM Employee WHERE Employee.id = ${req.params.employeeId}`,
            (error, employee) => {
                res.status(200).json({ employee: employee });
            });
        }
    });
});

/* DELETE
Updates the employee with the specified employee ID to be unemployed 
(is_current_employee equal to 0). Returns a 200 response.
If an employee with the supplied employee ID doesn’t exist, returns a 404 response*/
employeesRouter.delete('./:employeeId', (req, res, next) => {
    const sql = `UPDATE Employee SET is_current_employee = 0,
    WHERE Employee.id = $employeeId`;
    const value = {$employeeId: res.params.employeeId};
    db.run(sql, value, (error) => {
        if(error) {
            next(error);
        } else {
            db.get(`SELECT * FROM Employee WHERE Employee.id = ${req.params.employeeId}`,
            (error, employee) => {
                res.status(200).json({ employee: employee });
            });
        }
    });
});

module.exports = employeesRouter;