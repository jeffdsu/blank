blankApp.controller('homeMomentsController', ['$scope', '$resource', '$location', '$routeParams', '$http', '$interval', 'momentService', function ($scope, $resource, $location, $routeParams, $http, $interval, momentService) {
    
     momentService.get_collection()
     .then (function(moments){
         $scope.moments = moments
     }, function(err) {
         
     });
    
     $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };

    
     $scope.go_to_add_moment = function (moment) {
        $location.path('inspiration-corner/home/moments/add').replace();
    };
    
}]);
