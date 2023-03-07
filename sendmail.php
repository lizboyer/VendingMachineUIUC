<?php
// echo $email;

//   $email = $_POST['email'] ;
//   $message = $_POST['message'] ;

//   mail( "lizboyer01@gmail.com", "Feedback Form Results",
//     $message, "From: $email" );
//   header( "Location: http://www.google.com" );
?>


<?php
$echo("is running");
    $to = 'lizboyer01@gmail.com'; 
    $email = $_POST['email'] ;
    $subject = "VendingUIUC"; 
    
    $from = $_POST['realname'] ;
    $message = $_POST['message'] ;
    
    
    // Additional headers 
    //$headers = 'From: '.$fromName.'<'.$from.'>'; 
    
    // Send email 
    if(mail($to, $subject, $message, $headers)){ 
    echo 'Email has sent successfully.'; 
    }else{ 
    echo 'Email sending failed.'; 
    }
?>