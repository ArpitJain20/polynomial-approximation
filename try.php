


<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<form action="" method="post">
	<label>Enter C_id</label>
	<input type="text" name="cid"></input>
	<label>Select Degree</label>
<select name="deg">
<option value="1">1</option>
<option value="2">2</option>
  <option value="3">3</option>
  <option value="4">4</option>
  <option value="5">5</option>
  <option value="6">6</option>
  <option value="7">7</option>
  <option value="8">8</option>
  <option value="9">9</option>
  <option value="10">10</option>
  <option value="11">11</option>
  <option value="12">12</option>
  <option value="13">13</option>
  <option value="14">14</option>
  <option value="15">15</option>
</select>
<input type="submit" name="submit"></input>
</form>
<?php 

if(isset($_POST["submit"])){
	$x = $_POST['cid'];
$n = $_POST['deg'];

	$conn = mysqli_connect('localhost','root','','db');

$q="SELECT ad_time,avg(ad_valence) as avg_valence
FROM `analysis_detail_premium_v2` ad
  JOIN `analysis_results` ar ON ad.ad_ar_id=ar.ar_id
  JOIN `content_feedback` cf ON ar.ar_cf_id=cf.cf_id
  JOIN content c on c.c_id=cf.cf_c_id
WHERE cf.cf_c_id={$x} AND cf.cf_total_feedback_v2>=c.c_duration group by ad_time";
$res = mysqli_query($conn,$q);
$arr = array();
if($res->num_rows>0){
	while ($data = mysqli_fetch_assoc($res)) {
//		echo "<pre>";
//		print_r($data);
		array_push($arr, $data);
	}
}
	// echo $_POST['cid'];
	// echo $_POST['deg'];
	error_reporting(E_ALL ^ E_NOTICE);  
ini_set('display_errors', 1);
$out =fopen('data.csv','w');
for ($i=0; $i < count($arr); $i++) { 
	fputcsv($out, $arr[$i]);
	# code...
}
//fclose(fopen('data.csv','w'));

#'C:\\Python27\\python.exe C:\\xampp\\htdocs\\uprofile\\hello.py "'.$x.'"'
$poly=shell_exec('C:\\Python27\\python.exe C:\\xampp\\htdocs\\poly\\try.py "'.json_encode($arr).'"');

//$poly = explode("\n",$poly);
print_r($poly);
//





}


?>


<!-- <img src="graph.png">
<img src="graph6.png">
<img src="graph9.png">
<img src="graph12.png"> -->
</body>
</html>