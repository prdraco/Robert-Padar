<?php
namespace Codecademy;
function whatRelation($DNA) {
  if ($DNA === 100) {
    echo "identical twins";
  } elseif ($DNA >= 35 and $DNA <= 99) {
    echo "parent and child or full siblings";
  } elseif ($DNA >= 14 and $DNA <= 34) {
    echo "grandparent and grandchild, aunt/uncle and niece/nephew, or half siblings";
  } elseif ($DNA >= 6 and $DNA <= 13) {
    echo "first cousins";
  } elseif ($DNA >= 3 and $DNA <= 5) {
    echo "second cousins";
  } elseif ($DNA >= 1 and $DNA <= 2) {
    echo "third cousins";
  } else {
    echo "not genetically related";
  }
}

echo whatRelation(41); echo "\n";
echo whatRelation(100); echo "\n";

echo whatRelation(15); echo "\n";
echo whatRelation(7); echo "\n";
echo whatRelation(2); echo "\n";
