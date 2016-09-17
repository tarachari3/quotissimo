var app = angular.module("myapp", []);

app.controller('search', function($scope){
	$scope.querry={};
	$scope.message="";

	$scope.searchQuerry = function(){
		if (angular.equals({}, $scope.querry)) {
			$scope.message="please enter a twitter name";
			console.log('hi vinisha');
		}
		else {
			$scope.message="you rock";
			console.log($scope.message);
		}
	}
})
.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('//').endSymbol('//');
});

