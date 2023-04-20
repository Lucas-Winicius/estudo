class HomeController {
  index(req, res) {
    res.json({
      message: "Hello World! - HomeController",
    });
  }
}

export default new HomeController();
