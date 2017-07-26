/**
 * Created by sun on 7/18/2017.
 */

var alliedApp = angular.module('allied',['ngMaterial','ngMessages']);


//main controller
alliedApp.controller("alliedController",function ($scope,$http) {
                            // get func
                            $http.get("/api/get")
                                .then(function (response) {
                                    $scope.posts = response.data;
                                });
                            // // post func
                            //  var data = $.param({
                            //     fName: $scope.firstName,
                            //     lName: $scope.lastName
                            // });
                            //
                            // var config = {
                            //     headers : {ww
                            //         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                            //     }
                            // }
                            //
                            // $http.post('/ServerRequest/PostDataResponse', data, config)
                            // .success(function (data, status, headers, config) {
                            //     $scope.PostDataResponse = data;
                            // })
                        });

// filter bar controller
alliedApp.controller('filterbarCtrl', function($scope) {
    //date piocker
      this.myDate = "";
      this.isOpen = false;

    //date in out
      $scope.myDateStatus = 'Date in';
      $scope.dateStatus = [
          "Date in",
          "Date out",
      ];

    //status
      $scope.myStatus = 'Ready for review';
      $scope.statusDefult = [
          "All",
          "On rent",
          "Ready for review",
          "Pass",
          "Fail",
      ];

});

