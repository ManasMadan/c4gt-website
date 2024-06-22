<?php

/** PHPExcel_IOFactory */
require_once './excelinterop/phpexcel/Classes/PHPExcel/IOFactory.php';
require_once './excelinterop/phpexcel/socialcalc/socialcalc.inc';
require_once './excelinterop/phpexcel/socialcalc/sheetnode_phpexcel.import.inc';

$workbook = PHPExcel_IOFactory::load($argv['1']);

$numsheets = $workbook->getSheetCount();

$book = array();
$sheetarr = array();
 //$book['general']['numsheets'] = $numsheets;
 //$book['general']['currentname'] = $workbook->getActiveSheet()->getTitle();

$book['numsheets'] = $numsheets;
$book['currentname'] = $workbook->getActiveSheet()->getTitle();

 for ($s = 0; $s < $numsheets; $s++) {
    $sheet = $workbook->getSheet($s);
    $sheetsave = _sheetnode_phpexcel_import_do($workbook, $sheet);

    $title = $sheet->getTitle();

    //    echo $sheetsave;

    $sheetarr["Sheet".$s]['name'] = $title;
    $sheetarr["Sheet".$s]['sheetstr']['savestr'] = $sheetsave;
    if ($title == $book['currentname']) {
       $book['currentid'] = "sheet".$s;
    }   
}	
$book['sheetArr'] = $sheetarr;

$json = json_encode($book);
echo "$---$";
echo $json;


?>