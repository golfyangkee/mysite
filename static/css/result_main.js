<script>
  $(document).ready(function () {
    $(".tab_button > li").click(function () {
      var idx = $(this).index();

      $(this).addClass("on").siblings().removeClass("on");

      $(".tab_area .tab_cont")
        .eq(idx)
        .addClass("on")
        .siblings(".tab_cont")
        .removeClass("on");
    });
  });
</script>
