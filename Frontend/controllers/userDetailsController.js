blankApp.controller('userDetailsController', ['$scope', '$resource', '$routeParams', '$http', 'userService', function ($scope, $resource, $routeParams, $http, userService) {

    user_id = $routeParams.userId;
    
    userService.get(user_id)
    .then(function(data){
        $scope.user = data;
    }, function(err){
        
    });
    
    userService.get_insights(user_id)
    .then(function (data) {
                    $scope.insights = data;
                }, function (err) {

                })

}]);