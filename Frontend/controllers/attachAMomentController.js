blankApp.controller('attachAMomentController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'momentService', 'momentTypeService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, momentService, momentTypeService) {

    $scope.new = false;
    
    $scope.set_new = function () {
        $scope.new = !$scope.new;
    };
    momentTypeService.get_collection ()
    .then( function (moment_types) {
        $scope.moment_types = moment_types;
    }, function(err) {
        
    });
    
    momentService.get_collection ()
    .then( function (moments) {
        $scope.moments = moments;
    }, function(err) {
        
    });
    
    $scope.create_and_link_a_moment = function () {
        console.log($scope.moment);
        $scope.moment.insight = $scope.insight;
        momentService.create($scope.moment).then(function(moment) {
            console.log($scope.show);
            $scope.insight.moments.push(moment);
            $scope.show = false;
        }, function(err){});
    };
    
    
    $scope.attach_moment = function () {
        $scope.moment.insight = $scope.insight;
        momentService.update($scope.moment).then(function(moment) {
            console.log($scope.show);
            $scope.insight.moments.push(moment);
            $scope.show = false;
        }, function(err){});
    };
    
    

    

}]);