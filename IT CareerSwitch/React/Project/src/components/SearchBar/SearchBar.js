import React from 'react';
import './Search.css';

class SearchBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'term': '', 'location': '', 'sortBy':'best_match'};
        this.handleSerach = this.handleSerach.bind(this);
        this.handleTermChange = this.handleTermChange.bind(this);
        this.handleLocationChange = this.handleLocationChange.bind(this);
        this.sortByOptions = {
            'Best Match': 'best_match',
            'Highest Rated': 'rating',
            'Most Reviewed': 'review_count'
        }
        
    };

    handleSerach(event) {
        this.props.searchYelp(this.state.term, this.state.location, this.state.sortBy);
        event.preventDefault();
    }

    handleSortByChange(sortByOption) {
        this.setState({sortBy: sortByOption});
    }

    handleTermChange(event) {
        this.setState({term: event.target.value});
    }

    handleLocationChange(event) {
        this.setState({location: event.target.value});
    }

    getSortByClass(sortByOption) {
        if(this.state.sortBy === sortByOption) {
            return 'active';
        } else {
            return '';
        }
    }

    renderSortByOptions() {
        return Object.keys(this.sortByOptions).map(sortByOption => {
            let sortByOptionValue = this.sortByOptions[sortByOption];
            return <li onClick={this.handleSortByChange.bind(this, sortByOptionValue)} className={this.getSortByClass(sortByOptionValue)} key={sortByOptionValue}>{sortByOption}</li>;
        });
    };

    render() {
        return (
            <div className="SearchBar">
                <div className="SearchBar-sort-options">
                    <ul>
                        {this.renderSortByOptions()}
                    </ul>
                </div>
                <div className="SearchBar-fields">
                    <input onChange={this.handleTermChange} placeholder="Search Businesses" />
                    <input onChange={this.handleLocationChange} placeholder="Where?" />
                </div>
                <div className="SearchBar-submit">
                    <a onClick={this.handleSerach}>Let's Go</a>
                </div>
            </div>
        )
    }
};

export default SearchBar;