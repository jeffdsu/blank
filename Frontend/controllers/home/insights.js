blankApp.controller('homeInsightsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'profileService', function ($scope, $resource, $routeParams, $http, $interval, profileService) {
    
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
    

    
}]);