blankApp.controller('homeController', ['$scope', '$resource', '$routeParams', '$http', 'profileService', 'Auth', function ($scope, $resource, $routeParams, $http, profileService, Auth) {

    profileService.get_insights(1)
    .then(function(data){
        $scope.insights_personal = data;
    }, function(err){
        
    });
    
    profileService.get_insights(0)
    .then(function(data){
        $scope.insights_public = data;
    }, function(err){
        
    });
    
    $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };
    

}]);