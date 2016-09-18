var app = angular.module("myapp", []);

app.controller('search', function($scope, $http){
	$scope.querry={};
	$scope.message="Things Ann Coulter Thinks";
	$scope.song_url = "";
	$scope.profile_pic = "";
	$scope.background = "";

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
                		$('#background_image').css('background-image', 'url(' + $scope.background_image + ')');
                		$scope.song_url = res.song_url;
						$scope.profile_pic = res.profile_image;
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

