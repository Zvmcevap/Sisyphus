$(document).ready(function () {
  for (i = 1; i <= 31; i++) {
    console.log(i);
    $(".month").append(
      ` <div class="d-flex flex-column daysofmonth">
            <label for="${i}">
              ${i}
            </label>
            <input
              name="${i}"
              id="${i}"
              class="form-control-sm"
              type="checkbox"
            />
          </div>`
    );
  }
});
