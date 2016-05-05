blankApp.controller('adminInsightController', ['$scope', '$resource', '$routeParams', '$http', 'insightService', function ($scope, $resource, $routeParams, $http, insightService) {
    
    $scope.insights = [];
    
    insightService.get_collection()
        .then(function (data) {
                $scope.insights = data;
            }
            , function (err) {

            }
        );
    
    $scope.validate = function (id) {
        insightService.validate(id)
    }

}]);