blankApp.controller('attachToInsightController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'momentService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, momentService) {


    $scope.create_and_link_a_moment = function () {
        $scope.moment.insight = $scope.insight;
        momentService.create($scope.moment).then(function(moment) {
            console.log(moment);
        }, function(err){});
    };

    

}]);