<h1>Welcome to the Repetitive Cafe</h1>
<?php
$drinks = [
  'latte' => 2.49,
  'americano' => 1.99,
  'macchiato' => 2.99,
  'chokoccino'=> 3.29
  ];
$pastries = [
  "Croissant",
  "Muffin",
  "Slice of Pie",
  "Slice of Cake",
  "Cupcake",
  "Brownie"
];
?>

<h3><?=$drink?></h3>

<ul>
<?php foreach($drinks as $drink => $price):
?>
<li><?php echo $drink . " ", $price;?></li>
<?php endforeach;?>

</ul>
<h3>Pastries! ($2 each)</h3>

<ul>
<?php for($i=0; $i<count($pastries); $i++):?>
<li><?php echo $pastries[$i];?></li>
<?php endfor;?>
</ul>
