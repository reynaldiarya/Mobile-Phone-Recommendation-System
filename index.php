<?php
$latestphone = $_GET["latestphone"] ?? null;
if($latestphone != null){
    $command = 'python main.py ' . json_encode($latestphone);
    $output = exec($command);
    $recommendations = json_decode($output, true);
}
$command2 = 'python search.py';
$output2 = exec($command2);
$listphone = json_decode($output2, true);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mobile Recommendation System</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css" integrity="sha512-b2QcS5SsA8tZodcDtGRELiGv5SaKSk1vDHDaQRda0htPYWZ6046lr3kJ5bAAQdpV2mmA/4v0wQF9MyU6/pDIAg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css" integrity="sha512-nMNlpuaDPrqlEls3IX/Q56H36qvBASwb3ipuo3MxeWbsQB1881ox0cRv7UPTgBlriqoynt35KjEwgGUeUXIPnw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/select2-bootstrap-5-theme/1.3.0/select2-bootstrap-5-theme.min.css" integrity="sha512-z/90a5SWiu4MWVelb5+ny7sAayYUfMmdXKEAbpj27PfdkamNdyI3hcjxPxkOPbrXoKIm7r9V2mElt5f1OtVhqA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        .select2-results__option{
            color: #000;
        }
        .select2-container{
            margin-bottom: 10px;
        }
        .select2-container .select2-selection--single{
            height: 32px;
        }
    </style>
</head>

<body class="bg-dark text-white">
    <div class="text-center mt-5 mb-0">
        <h1>Mobile Recommendation System</h1>
    </div>
    <div class="container d-flex justify-content-center bg-blue">
        <div class="col-lg-4 my-5">
            <form action="index.php" method="get">
                <select class="js-example-basic-single" style="color: black; width: 100%; height: 100px" name="latestphone">
                <?php
                    foreach ($listphone as $list) {
                    echo <<<HTML
                        <option value="$list">$list</option>
                    HTML;
                    }
                ?>
                </select>
                <button type="submit mt-5" class="btn btn-outline-primary">Recommendation</button>
            </form>
        </div>
    </div>
    <div class="container">
        <?php
        if ($latestphone != null) {
            echo <<<HTML
                <h2 class="text-center">Mobile Phone Recommendations Other than  $latestphone</h2>
            HTML;
        } else {
            echo <<<HTML
                <h2 class="text-center">Choose a mobile first</h2>
            HTML;
        }
        ?>
        <div class="row">
            <?php
            if($latestphone != null){
                foreach ($recommendations['name'] as $key => $name) {
                    $price = number_format($recommendations['price'][$key], 2, '.', ',');
                    $storage = $recommendations['Storage'][$key];
                    $ram = $recommendations['RAM'][$key];
                    $rating = $recommendations['ratings'][$key];
                    $image = $recommendations['imgURL'][$key];
                    // echo "Name: $name, Price: $price<br>";

                    // Generate HTML for each recommendation
                    echo <<<HTML
                        <div class="col-lg-3 my-3">
                            <div class="card p-5 text-center h-100">
                                <img class="w-75 mx-auto" src="$image" style="height: 250px" alt="" />
                                <div class="card-body">
                                    <h5 class="card-title">$name</h5>
                                    <p class="card-text mt-0 mb-3">Price: ₹$price</p>
                                    <p class="card-text mb-0">Storage: $storage GB</p>
                                    <p class="card-text mb-0">RAM: $ram GB</p>
                                    <p class="card-text mb-0">Rating: $rating</p>
                                </div>
                            </div>
                        </div>
                        HTML;
                }
            }
            ?>
        </div>
    </div>
    <footer class="py-3">
        <p class="border-top pt-4 text-center mt-5 mb-0">&copy; 2023 D4 Teknik Informatika Universitas Airlangga</p>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/js/bootstrap.min.js" integrity="sha512-WW8/jxkELe2CAiE4LvQfwm1rajOS8PHasCCx+knHG0gBHt8EXxS6T6tJRTGuDQVnluuAvMxWF4j8SNFDKceLFg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js" integrity="sha512-2ImtlRlf2VVmiGZsjm9bEyhjGW4dU7B6TNwh/hx/iSByxNENtj3WVE6o/9Lj4TJeVXPi4bnOIMXFIJJAeufa0A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
        // In your Javascript (external .js resource or <script> tag)
    $(document).ready(function() {
        $('.js-example-basic-single').select2();
    });
    </script>
</body>

</html>