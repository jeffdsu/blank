blankApp.controller('contributorDetailsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'contributorService', function ($scope, $resource, $routeParams, $http, $interval, contributorService) {
    
    self = this;
    contributorId = $routeParams.contributorId;
        
     contributorService.get(contributorId)
        .then(function (data) {
                $scope.contributor = data;
            }
            , function (err) {

            }
        );
    
    contributorService.get_books(contributorId)
    .then(function (data) {
                $scope.works = data;
            }
            , function (err) {

            }
        );

    
}]);
