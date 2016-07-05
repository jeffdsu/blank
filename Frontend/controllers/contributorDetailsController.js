blankApp.controller('contributorDetailsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'contributorService', function ($scope, $resource, $routeParams, $http, $interval, contributorService) {
    
    self = this;
    contributorId = $routeParams.contributorId;
    console.log(contributorId);
        
     contributorService.get(contributorId)
        .then(function (data) {
                $scope.contributor = data;
            }
            , function (err) {

            }
        );
    
    contributorService.get_media(contributorId)
    .then(function (data) {
                $scope.works = data;
            }
            , function (err) {

            }
        );

    
}]);
