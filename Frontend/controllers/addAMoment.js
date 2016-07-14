blankApp.controller('addAMomentController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'momentService', 'momentTypeService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, momentService, momentTypeService) {

    $scope.new_moment = momentService.new_moment;
    
    momentTypeService.get_collection ()
    .then( function (moment_types) {
        $scope.moment_types = moment_types;
    }, function(err) {
        
    });
    
    $scope.create_a_moment = function () {
        console.log($scope.new_moment);
        $scope.new_moment.insight = $scope.insight;
        momentService.create($scope.new_moment).then(function(new_moment) {
            momentService.new_moment = Object();
            $location.path('inspiration-corner/home/moments').replace();
        }, function(err){});
    };
    
    
    

    

}]);