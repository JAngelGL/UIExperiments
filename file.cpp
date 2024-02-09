using System;
using System.Diagnostics;
using System.IO;

class Program
{
    static void Main()
    {
        // Intenta encontrar el intérprete de Python en el sistema
        string pythonPath = FindPythonInterpreter();

        if (pythonPath != null)
        {
            // Ruta al script de Python que quieres ejecutar
            string scriptPath = "Ruta\\al\\tu_script.py";

            // Crear un proceso para ejecutar el script de Python
            ProcessStartInfo psi = new ProcessStartInfo(pythonPath, scriptPath)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process process = new Process() { StartInfo = psi })
            {
                process.Start();

                // Puedes leer la salida estándar si es necesario
                string output = process.StandardOutput.ReadToEnd();

                process.WaitForExit();
            }
        }
        else
        {
            Console.WriteLine("Intérprete de Python no encontrado.");
        }
    }

    static string FindPythonInterpreter()
    {
        // Intenta encontrar el intérprete de Python en el PATH del sistema
        string pythonPath = FindInPath("python.exe");

        // Si no se encuentra en el PATH, intenta encontrarlo en ubicaciones comunes
        if (pythonPath == null)
        {
            string[] commonPaths = { @"C:\Python39\python.exe", @"C:\Python38\python.exe", @"C:\Python37\python.exe" };

            foreach (var path in commonPaths)
            {
                if (File.Exists(path))
                {
                    pythonPath = path;
                    break;
                }
            }
        }

        return pythonPath;
    }

    static string FindInPath(string fileName)
    {
        var paths = Environment.GetEnvironmentVariable("PATH");
        foreach (var path in paths.Split(Path.PathSeparator))
        {
            var fullPath = Path.Combine(path, fileName);
            if (File.Exists(fullPath))
            {
                return fullPath;
            }
        }
        return null;
    }
}
