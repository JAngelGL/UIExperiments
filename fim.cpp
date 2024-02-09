using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // Ruta al archivo de script de Python
        string scriptPath = @"C:\Ruta\Al\Archivo\Script.py";

        // Crear un proceso de Python
        ProcessStartInfo psi = new ProcessStartInfo
        {
            FileName = "python", // Asegúrate de que "python" esté en el PATH del sistema
            Arguments = scriptPath,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using (Process process = new Process { StartInfo = psi })
        {
            // Iniciar el proceso
            process.Start();

            // Leer la salida estándar y la salida de error (opcional)
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            // Esperar a que el proceso termine
            process.WaitForExit();

            // Mostrar la salida y los errores (puedes personalizar esta parte según tus necesidades)
            Console.WriteLine("Salida del script:");
            Console.WriteLine(output);

            if (!string.IsNullOrEmpty(error))
            {
                Console.WriteLine("Errores del script:");
                Console.WriteLine(error);
            }
        }
    }
}
