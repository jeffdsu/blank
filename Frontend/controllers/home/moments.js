blankApp.controller('homeMomentsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'momentService', function ($scope, $resource, $routeParams, $http, $interval, momentService) {
    
     momentService.get_collection()
     .then (function(moments){
         $scope.moments = moments
     }, function(err) {
         
     });
    
     $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };

    
}]);
