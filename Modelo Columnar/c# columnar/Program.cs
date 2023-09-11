using Cassandra;
using Cassandra.Data.Linq;
using System;
using System.Linq;
using Newtonsoft.Json;
using System.IO;



namespace CassandraCSharpExample
{
    class Program
    {
        static void Maina(string[] args)
        {
            // Configura la conexión a tu clúster de Cassandra
            var cluster = Cluster.Builder().AddContactPoint("127.0.0.1").Build();
            var session = cluster.Connect("dbcolumnas"); // Reemplaza "dbcolumnas" con tu keyspace

            // Cargar datos desde un archivo JSON a un objeto en C#
            var departamentosJson = File.ReadAllText("Tablas/departamentos.json");
            var departamentos = JsonConvert.DeserializeObject<Departamento[]>(departamentosJson);

            var municipiosJson = File.ReadAllText("Tablas/municipios.json");
            var municipios = JsonConvert.DeserializeObject<Municipio[]>(municipiosJson);

            var beneficiarioJson = File.ReadAllText("Tablas/beneficiario.json");
            var beneficiarios = JsonConvert.DeserializeObject<Beneficiario[]>(beneficiarioJson);

            var programaJson = File.ReadAllText("Tablas/programa.json");
            var programas = JsonConvert.DeserializeObject<Programa[]>(programaJson);

            // Define las tablas en Cassandra una por una
            session.Execute(@"
                CREATE TABLE IF NOT EXISTS Departamento (
                    id UUID PRIMARY KEY,
                    codigodepartamentoatencion VARCHAR,
                    nombredepartamentoatencion VARCHAR
                ) WITH comment = 'Tabla de departamentos';
            ");

            session.Execute(@"
                CREATE TABLE IF NOT EXISTS Municipio (
                    id UUID PRIMARY KEY,
                    codigomunicipioatencion VARCHAR,
                    nombremunicipioatencion VARCHAR,
                    codigodepartamentoatencion VARCHAR
                ) WITH comment = 'Tabla de municipios';
            ");

            session.Execute(@"
                CREATE TABLE IF NOT EXISTS Beneficiario (
                    id UUID PRIMARY KEY,
                    idBeneficiario INT,
                    bancarizado VARCHAR,
                    discapacidad VARCHAR,
                    etnia VARCHAR,
                    genero VARCHAR,
                    nivelescolaridad VARCHAR,
                    pais VARCHAR,
                    tipodocumento VARCHAR,
                    titular VARCHAR,
                    codigomunicipioatencion VARCHAR,
                    estadobeneficiario VARCHAR,
               ) WITH comment = 'Tabla de beneficiarios';
            ");

            session.Execute(@"
                CREATE TABLE IF NOT EXISTS Programa (
                    id UUID PRIMARY KEY,
                    idPrograma INT,
                    tipoasignacionbeneficio VARCHAR,
                    fechainscripcionbeneficiario VARCHAR,
                    tipobeneficio VARCHAR,
                    tipopoblacion VARCHAR,
                    rangobeneficioconsolidadoasignado VARCHAR,
                    rangoultimobeneficioasignado VARCHAR,
                    FechaUltimoBeneficioAsignado VARCHAR,
                    idBeneficiario INT,
                    RangoEdad VARCHAR,
                    CantidadDeBeneficiarios INT
                ) WITH comment = 'Tabla de programas';
            ");

            // Crear objetos de tabla en Cassandra
            var departamentoTable = new Table<Departamento>(session);
            var municipioTable = new Table<Municipio>(session);
            var beneficiarioTable = new Table<Beneficiario>(session);
            var programaTable = new Table<Programa>(session);

            // Insertar datos en las tablas de Cassandra
            foreach (var departamento in departamentos)
            {
                departamento.id = Guid.NewGuid();
                departamentoTable.Insert(departamento).Execute();
            }

            foreach (var municipio in municipios)
            {
                municipio.id = Guid.NewGuid();
                municipioTable.Insert(municipio).Execute();

            }

            int index = 1;

            foreach (var beneficiario in beneficiarios)
            {
               
                beneficiario.id = Guid.NewGuid();

                beneficiario.idBeneficiario = index;
                beneficiarioTable.Insert(beneficiario).Execute();
                index++;
              
            }

            int i = 1;

            foreach ( var programa in programas)
            {
                programa.id = Guid.NewGuid();
                programa.idBeneficiario= i;
                programa.idPrograma = i;
                programaTable.Insert(programa).Execute();
                i++;

            }

            // Cerrar la conexión
            cluster.Dispose();

            Console.WriteLine("Datos insertados en la base de datos Cassandra.");
            Console.ReadKey();
        }
    }

    // Define las clases para mapear los datos
    public class Departamento
    {
        // Propiedades que coinciden con las columnas de la tabla Departamento
        public Guid id { get; set; }
        public string codigodepartamentoatencion { get; set; }
        public string nombredepartamentoatencion { get; set; }
    }

    public class Municipio
    {
        // Propiedades que coinciden con las columnas de la tabla Municipio
        public Guid id { get; set; }
        public string codigomunicipioatencion { get; set; }
        public string nombremunicipioatencion { get; set; }
        public string codigodepartamentoatencion { get; set; }
    }

    public class Beneficiario
    {
        // Propiedades que coinciden con las columnas de la tabla Beneficiario
        public Guid id { get; set; }
        public int idBeneficiario { get; set; }
        public string bancarizado { get; set; }
        public string discapacidad { get; set; }
        public string etnia { get; set; }
        public string genero { get; set; }
        public string nivelescolaridad { get; set; }
        public string pais { get; set; }
        public string tipodocumento { get; set; }
        public string titular { get; set; }
        public string codigomunicipioatencion { get; set; }
        public string estadobeneficiario { get; set; }
    }

    public class Programa
    {
        // Propiedades que coinciden con las columnas de la tabla Programa
        public Guid id { get; set; }
        public int idPrograma { get; set; }
        public string fechainscripcionbeneficiario { get; set; }
        public string tipoasignacionbeneficio { get; set; }
        public string tipobeneficio { get; set; }
        public string tipopoblacion { get; set; }
        public string rangobeneficioconsolidadoasignado { get; set; }
        public string rangoultimobeneficioasignado { get; set; }
        public string fechaultimobeneficioasignado { get; set; }
        
        public int idBeneficiario { get; set; }
        public string rangoedad { get; set; }
        public int cantidaddebeneficiarios { get; set; }
    }
}
