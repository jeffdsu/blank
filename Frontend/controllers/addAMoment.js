blankApp.controller('addAMomentController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'momentService', 'momentTypeService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, momentService, momentTypeService) {


    
    momentTypeService.get_collection ()
    .then( function (moment_types) {
        $scope.moment_types = moment_types;
    }, function(err) {
        
    });
    
    $scope.create_a_moment = function () {
        console.log($scope.moment);
        $scope.moment.insight = $scope.insight;
        momentService.create($scope.moment).then(function(moment) {
            console.log($scope.show);
            $location.path('inspiration-corner/home/moments').replace();
        }, function(err){});
    };
    
    
    

    

}]);