<?php

echo date('Ymd H:i:s',strtotime('20170202'));


$date=new DateTime();
$date->modify('this week');
$first_day_of_week=$date->format('Y-m-d');
echo $first_day_of_week;


echo 7200000;



