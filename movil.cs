using OpenQA.Selenium.Appium.Windows;
using OpenQA.Selenium.Remote;

namespace PruebasAppium
{
    [TestClass]
    public class PruebasAppium
    {
        private const string WindowsApplicationDriverUrl = "http://127.0.0.1:4723";
        private const string WindowsApplicationId = "TuAppId"; // Reemplaza con el identificador de tu aplicación

        protected static WindowsDriver<WindowsElement> session;

        [ClassInitialize]
        public static void Setup(TestContext context)
        {
            DesiredCapabilities appCapabilities = new DesiredCapabilities();
            appCapabilities.SetCapability("app", WindowsApplicationId);
            session = new WindowsDriver<WindowsElement>(new Uri(WindowsApplicationDriverUrl), appCapabilities);
        }

        [TestMethod]
        public void TestClickButton()
        {
            WindowsElement button = session.FindElementByAccessibilityId("BotonId"); // Reemplaza con el identificador de tu botón
            button.Click();
            // Agrega aserciones para validar el resultado de la acción
        }

        [ClassCleanup]
        public static void TearDown()
        {
            session.Dispose();
        }
    }
}
