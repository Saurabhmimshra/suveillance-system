<?php

?>
<html>
	<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
	</head>
	<body>

<div class="head">
	<h2>Hack-VSIT.</h2>
				<center><h1>Welcome to Sarvgamya surveillance System</h1></center>
					<!-- <div class=" row-mt-15em"> --><br>
					</div>

						<img src="img.jpg" width='1400px' height='410px'>
						<br>
						<form action="index.php" method="post">

												<div class="row form-group">
													<div class="col-md-12">
														<input type="text" name="temp" value="bhai" hidden><br>
													<center>	<button class="btn" type="submit" name="submit" value="Submit">Launch surveillance System</center>
													</div>
												</div>
											</form>

		<div class="team">
			<h2>Team-Vision</h2>
		</div>


	</body>
	<style>
	/* Material style */
	/* Material style */
button {
  border: none;
  cursor: pointer;
  color: white;
  padding: 15px 40px;
  border-radius: 2px;
  font-size: 22px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, .4);
  background: #2196F3;
}

.team {
  position: fixed;
  right: 2px;
  bottom: 0px;
}

/* Ripple magic */
button{
  position: relative;
  overflow: hidden;
}

button:after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 5px;
  height: 5px;
  background: rgba(255, 255, 255, .5);
  opacity: 0;
  border-radius: 100%;
  transform: scale(1, 1) translate(-50%);
  transform-origin: 50% 50%;
}

@keyframes ripple {
  0% {
    transform: scale(0, 0);
    opacity: 1;
  }
  20% {
    transform: scale(25, 25);
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: scale(40, 40);
  }
}

button:focus:not(:active)::after {
  animation: ripple 1s ease-out;
}

h1,h2{
	font-family: sans-serif;
	color: white;
}
body
{
	background-color: rgb(22,17,40);
}
</style>
</html>
<?php

	if(isset($_POST['temp'])){
 		 echo '<pre>';

// Outputs all the result of shellcommand "ls", and returns
// the last output line into $last_line. Stores the return value
// of the shell command in $retval.
		@$last_line = system('python motiondetector2.py', $retval);
//python motiondetector2.py
// Printing additional infopython motiondetector2.py
			echo '
			</pre>';

			//header("Location: index.php");

	}
?>
