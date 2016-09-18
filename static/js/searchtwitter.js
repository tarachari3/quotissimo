var app = angular.module("myapp", []);

app.controller('search', function($scope, $http){
	$scope.querry={};
	$scope.message="Things A Twitter Person Might Think";
	$scope.song_url = "";
	$scope.profile_pic = "https://pbs.twimg.com/profile_images/597794910155210752/yCf0aPVL.png";
	$scope.background_image = "../static/img/lavender.jpg";

	$scope.searchQuerry = function(){
		if (angular.equals({}, $scope.querry)) {
			$scope.message="please enter a twitter name";
		}
		else {
            $http({
              method: 'POST',
              url: '/quoteGen',
              data: angular.toJson($scope.querry)
            }).then(function successCallback(response) {
                if (response.data != undefined) {
                	var res = angular.fromJson(response.data);
                	if (res.error != undefined) {
                		 $scope.message = res.error;
                	} else {
                		$scope.message = res.final_quote;
                		$scope.song_url = res.song_url;
						$scope.profile_pic = res.profile_image;
						$scope.background = res.background_image; // change to scope.background_image ??
                	}
                }

              }, function errorCallback(response) {
                $scope.message = 'Query failed, please try again.';
              });	
		}
	}
})
.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('//').endSymbol('//');
});

