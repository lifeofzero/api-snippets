<?php
// Download the **Next-Gen** twilio-php library from:
// twilio.com/docs/libraries/php#installation-nextgen

// Include dependencies from Composer's autoload (including Twilio library)
include 'vendor/autoload.php';

$sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";  // Your Account SID from www.twilio.com/console
$token = "your_auth_token"; // Your Auth Token from www.twilio.com/console

$client = new Twilio\Rest\Client($sid, $token);

$cmd = $client->preview->wireless->commands("DCcb6aa7c620874dd98ba6c9c4108d0ed0")->fetch();

echo $cmd->command, "\n";