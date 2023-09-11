using Cassandra;
using Cassandra.Data.Linq;
using CassandraCSharpExample;
using System;
using System.Linq;


namespace columnas
{
    class consultas
    {
        static void Main(string[] args)
        {
            // Configura la conexión a tu clúster de Cassandra
            var cluster = Cluster.Builder()
                .AddContactPoint("127.0.0.1")
                .Build();


            var session = cluster.Connect("dbcolumnas");

            /*
             //¿Cuántos tipos de población hay y cuales son?

            var consulta = "SELECT tipopoblacion FROM Programa"; // Ajusta la consulta según tu modelo

            var resultados = session.Execute(consulta);

            // Crear un conjunto para almacenar tipos de población únicos
            var tiposDePoblacionUnicos = new HashSet<string>();

            foreach (var fila in resultados)
            {
                // Accede al valor de "tipopoblacion"
                var tipoPoblacion = fila.GetValue<string>("tipopoblacion");

                // Agrega el tipo de población al conjunto si es diferente de nulo
                if (!string.IsNullOrEmpty(tipoPoblacion))
                {
                    tiposDePoblacionUnicos.Add(tipoPoblacion);
                }
            }

            // Imprime la cantidad de tipos de población y la lista de tipos
            Console.WriteLine($"Cantidad de tipos de población: {tiposDePoblacionUnicos.Count}");
            Console.WriteLine("Tipos de población:");

            foreach (var tipo in tiposDePoblacionUnicos)
            {
                Console.WriteLine(tipo);
            }
            */


            /*
              //  ¿Cuál es el rango más alto de beneficio consolidado asignado?

              var consulta = "SELECT rangobeneficioconsolidadoasignado FROM Programa";

              var resultados = session.Execute(consulta);

              // Almacena los rangos en una lista
              var rangos = new List<string>();

              foreach (var fila in resultados)
              {
                  var rango = fila.GetValue<string>("rangobeneficioconsolidadoasignado");
                  rangos.Add(rango);
              }

              // Encuentra el rango más alto en la lista
              var rangoMasAlto = rangos.Count > 0 ? rangos.Max() : "No hay datos";

              Console.WriteLine($"Rango más alto de beneficio consolidado asignado: {rangoMasAlto}");

              */

            /*
            // programas con el limite mas alto de beneficiario cuando el tipo de asignacion es MONETARIO


            var consulta = "SELECT id, tipoasignacionbeneficio, cantidaddebeneficiarios FROM Programa WHERE tipoasignacionbeneficio = 'MONETARIO' ALLOW FILTERING";

            // Ejecutar la consulta en Cassandra
            var resultados = session.Execute(consulta);

           // Crear una lista para almacenar programas como tuplas (ID, Tipo de Asignación, Cantidad de Beneficiarios)
           var programas = new List<Tuple<Guid, string, int>>();

           // Iterar a través de los resultados de la consulta
           foreach (var fila in resultados)
           {
              // Obtener el ID, Tipo de Asignación y Cantidad de Beneficiarios de cada fila
             var id = fila.GetValue<Guid>("id");
             var tipoAsignacion = fila.GetValue<string>("tipoasignacionbeneficio");
             var cantidad = fila.GetValue<int>("cantidaddebeneficiarios");

             // Agregar los datos como una tupla a la lista de programas
             programas.Add(new Tuple<Guid, string, int>(id, tipoAsignacion, cantidad));
           }

             // Ordenar la lista de programas por la cantidad de beneficiarios en orden descendente
             programas.Sort((a, b) => b.Item3.CompareTo(a.Item3));

              // Encontrar el límite más alto de beneficiarios
              var limiteMasAlto = programas.Any() ? programas[0].Item3 : 0;

              // Mostrar el límite más alto de beneficiarios en la consola
              Console.WriteLine($"El límite más alto de beneficiarios es: {limiteMasAlto}");

              // Verificar si hay programas con el límite más alto
             if (programas.Any())
             {
               // Mostrar programas con el límite más alto de beneficiarios y sus detalles
               Console.WriteLine("Programas con el límite más alto de beneficiarios:");

                foreach (var programa in programas)
                 {
                    Console.WriteLine($"ID: {programa.Item1}, Tipo de Asignación: {programa.Item2}, Cantidad de Beneficiarios: {programa.Item3}");
                 }
             }
             else
             {
                // Mostrar un mensaje si no se encontraron programas con asignación 'MONETARIO'
                Console.WriteLine("No se encontraron programas con el tipo de asignación 'MONETARIO'.");
             }

             */

            /*
            // columnas de la tabla Programa
            var consulta = "SELECT * FROM Programa LIMIT 1";
            var resultados = session.Execute(consulta);

            var metadata = resultados.Columns;

            foreach (var columna in metadata)
            {
                Console.WriteLine(columna.Name);
            }

            */




            /*
            //¿Cuántos beneficiarios se encuentran bancarizados?

            var consulta = "SELECT COUNT(*) AS cantidad_bancarizados FROM Beneficiario WHERE bancarizado = 'SI' ALLOW FILTERING";

            var resultados = session.Execute(consulta);

            foreach (var fila in resultados)
            {
                var cantidadBancarizados = fila.GetValue<long>("cantidad_bancarizados");

                Console.WriteLine($"Cantidad de beneficiarios bancarizados: {cantidadBancarizados}");
            }

            */

            
            // ¿Cuánto beneficiarios hay por cada género?
     
            var consulta = "SELECT genero FROM Beneficiario";

            var resultados = session.Execute(consulta);

            // Almacena los géneros en una lista
            var generos = new List<string>();

            foreach (var fila in resultados)
            {
                var genero = fila.GetValue<string>("genero");
                generos.Add(genero);
            }

            // Realiza la agregación de la cantidad de beneficiarios por género
            var conteoPorGenero = new Dictionary<string, int>();

            foreach (var genero in generos)
            {
                if (conteoPorGenero.ContainsKey(genero))
                {
                    conteoPorGenero[genero]++;
                }
                else
                {
                    conteoPorGenero[genero] = 1;
                }
            }

            // Muestra la cantidad de beneficiarios por género
            Console.WriteLine("Cantidad de beneficiarios por género:");

            foreach (var kvp in conteoPorGenero)
            {
                Console.WriteLine($"Género: {kvp.Key}, Cantidad de beneficiarios: {kvp.Value}");
            }
            


            /*
            // nombre de los departamentos?

                         // Define la tabla de departamentos
                         var departamentoTable = new Table<Departamento>(session);

                         // Realiza la consulta para obtener los nombres de los departamentos
                         var query = departamentoTable.Select(d => new { d.nombredepartamentoatencion });

                         // Ejecuta la consulta y obtén los resultados
                         var results = query.Execute();

                         // Imprime los nombres de los departamentos
                         foreach (var result in results)
                         {
                             Console.WriteLine(result.nombredepartamentoatencion);
                         }

              */


            /* //tabla departamento
                // Define la tabla de departamentos
                var departamentoTable = new Table<Departamento>(session);

                // Realiza la consulta para obtener todos los atributos de los departamentos
                var query = departamentoTable.Select(d => d);

                // Ejecuta la consulta y obtén los resultados
                var results = query.Execute();

                        // Imprime todos los atributos de los departamentos
                        foreach (var result in results)
                        {
                            Console.WriteLine($"ID: {result.id}, Código Departamento: {result.codigodepartamentoatencion}, Nombre Departamento: {result.nombredepartamentoatencion}");
                        }

                        */
            // Cerrar la conexión
            cluster.Dispose();

            Console.WriteLine("Consulta finalizada.");
            Console.ReadKey();
        }
    }
}