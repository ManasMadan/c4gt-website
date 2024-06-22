<?php

require_once './excelinterop/phpexcel/Classes/PHPExcel/IOFactory.php';
require_once './excelinterop/phpexcel/Classes/PHPExcel.php';
require_once './excelinterop/phpexcel/socialcalc/socialcalc.inc';
require_once './excelinterop/phpexcel/socialcalc/sheetnode_phpexcel.export.inc';



// read the tmp file
$fname = $argv['1'];
$outfile = $argv['2'];
$outfiletype = $argv['3'];

$fh = fopen($fname, "r");
$data = fread($fh, filesize($fname));
fclose($fh);

//echo $data;

$book = json_decode($data);

//var_dump($book);
//print $book->{"numsheets"};
//print $book->{"currentid"};
$sheetarr = $book->{"sheetArr"};
//var_dump($sheetarr)

$workbook = new PHPExcel();

$sindex = 0;
$actualactiveindex = 0;

foreach ($sheetarr as $key => $value) {
    //var_dump($key);
    //var_dump($value);
    if ($sindex > 0) {
       $workbook->createSheet();
       $workbook->setActiveSheetIndex($sindex);
    } 
    if ($key == $book->{"currentid"}) {
       $actualactiveindex = $sindex;
    }   

    //var_dump($value->{"name"});

    $title = $value->{"name"};
    $sheet = socialcalc_parse_sheet($value->{"sheetstr"}->{"savestr"});

    _sheetnode_phpexcel_export_do($workbook, $title, $sheet);

    $sindex = $sindex + 1;

    echo $sindex.'done'."\n";
        
}
$workbook->setActiveSheetIndex($actualactiveindex);

// write the workbook into a file
$objWriter = PHPExcel_IOFactory::createWriter($workbook, $outfiletype);
$objWriter->save($outfile);

?>
