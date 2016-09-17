var app = angular.module("myapp", []);

app.controller('search', function($scope, $http){
	$scope.querry={};
	$scope.message="";

	$scope.searchQuerry = function(){
		if (angular.equals({}, $scope.querry)) {
			$scope.message="please enter a twitter name";
		}
		else {
            $http({
              method: 'POST',
              url: '/quoteGen',
              data: $scope.querry
            }).then(function successCallback(response) {
                // this callback will be called asynchronously when the response is available
                if (response.data.result != undefined) {
                    $scope.message = response.data.result;
                } else if (response.data.redirect == true) {
                    window.location = '/'
                } else {
                  $scope.message = "Login Failed, please try again."
                }

              }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                $scope.message = 'Login Failed, please try again.';
              });	
		}
	}
})
.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('//').endSymbol('//');
});

