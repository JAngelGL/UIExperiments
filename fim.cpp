using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // Ruta completa del archivo Python
        string pythonPath = "ruta\\a\\python.exe";  // Cambia esto por la ruta real de tu instalación de Python
        string scriptPath = "ruta\\del\\script.py"; // Cambia esto por la ruta de tu script Python

        // Argumentos del proceso Python (ruta del script)
        string arguments = $"\"{scriptPath}\"";

        // Configurar el proceso de inicio
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = pythonPath,
            Arguments = arguments,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        // Iniciar el proceso
        using (Process process = new Process { StartInfo = startInfo })
        {
            process.Start();

            // Leer la salida estándar y la salida de error
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            process.WaitForExit();

            // Imprimir la salida y los errores (si los hay)
            Console.WriteLine("Salida del script:");
            Console.WriteLine(output);

            if (!string.IsNullOrEmpty(error))
            {
                Console.WriteLine("Errores:");
                Console.WriteLine(error);
            }
        }
    }
}
