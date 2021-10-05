using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EscaneoDeImagenes
{
    public partial class Form1 : Form
    {
        Bitmap loadedImage_bpm, generatedImage_bpm;
        int alto, ancho;
        
       

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }




        private void bt_Importar_Click(object sender, EventArgs e)
        {


            OpenFileDialog ofd = new OpenFileDialog();
            if(ofd.ShowDialog() == DialogResult.OK)
            {
                loadedImage_bpm = new Bitmap(Image.FromFile(ofd.FileName));
                pictureBox1.Image = loadedImage_bpm;

                alto = loadedImage_bpm.Height;
                ancho = loadedImage_bpm.Width;
            }



            bt_Scan.Enabled = true;
            bt_GetPixel.Enabled = true;
            bt_WriteData.Enabled = true;
            


        }


        private void bt_GetPixel_Click(object sender, EventArgs e)
        {
            for (int y = 0; y < loadedImage_bpm.Height; y++)
            {
                for (int x = 0; x < loadedImage_bpm.Width; x++)
                {
                     Color color = loadedImage_bpm.GetPixel(x, y);
                    int a = color.A;
                    int r = color.R;
                    int g = color.G;
                    int b = color.B;
                    Console.WriteLine(a + "," + r + "," + g + "," + b );

                }
                Console.WriteLine("- - - - -\n");
            }

            MessageBox.Show("ESCANEADO COMPLETO :)");
            bt_GetPixel.Enabled = false;
        }

        private void bt_WriteData_Click(object sender, EventArgs e)
        {
            TextWriter escribir1 = new StreamWriter("D:\\Modular\\Imagen\\IMAGE DATA\\DataPixelARGB_" + alto + "x" + ancho + ".txt");
            escribir1.WriteLine(loadedImage_bpm.Height);
            escribir1.WriteLine(loadedImage_bpm.Width);

            for (int y = 0; y < loadedImage_bpm.Height; y++)
            {
                for (int x = 0; x < loadedImage_bpm.Width; x++)
                {
                    Color color1 = loadedImage_bpm.GetPixel(x, y);
                    int a = color1.A;
                    int r = color1.R;
                    int g = color1.G;
                    int b = color1.B;
                    escribir1.WriteLine(a + "," + r + "," + g + "," + b);
                }
                //escribir1.WriteLine("-");
            }

            escribir1.Close();

            MessageBox.Show("ARCHIVO PIXEL DATA GENERADO");

            bt_WriteData.Enabled = false;
        }


        private void bt_Scan_Click(object sender, EventArgs e)
        {
            //Create MemoryStream
            var ms = new MemoryStream(); //aqui van los bytes

            //guardando bytes a ms
            loadedImage_bpm.Save(ms, System.Drawing.Imaging.ImageFormat.Jpeg);

            byte[] bytes = ms.ToArray();


            Console.WriteLine(bytes);

            //Writing the file

            string ruta = ("D:\\Modular\\Imagen\\IMAGE DATA\\ByteArrayData_" + alto + "x" + ancho + ".txt");
            File.WriteAllBytes(ruta, bytes);

            MessageBox.Show("Escaneado Y Escrito :)");
            bt_Scan.Enabled = false;

        }

        private void btGenerateFromData_Click(object sender, EventArgs e)
        {
            byte[] array;
            string filename;

            using (OpenFileDialog openFileDialog1 = new OpenFileDialog())
            {
                if (openFileDialog1.ShowDialog() != DialogResult.OK)
                    return;
                filename = openFileDialog1.FileName;
                array = File.ReadAllBytes(filename);
            }
            var imageMS = new MemoryStream(array);

            //create image from stream
            Image imgFromStream = Image.FromStream(imageMS);
            pictureBox2.Image = imgFromStream;

            MessageBox.Show("Generada :)");
        }

        private void bt_GenerateFromARGB_Click(object sender, EventArgs e)
        {
            OpenFileDialog opfd = new OpenFileDialog();
            opfd.Title = "Importe el Txt Con Valores ARGB";
            

            string linea ="";//Cadena donde se almacena una linea completa del archivo

            char delimitador = ',';
            string[] argb_segments;
            int y_Height = 0;
            int x_Widht = 0;


            if(opfd.ShowDialog() == DialogResult.OK)
            {
                StreamReader sr = new StreamReader(opfd.FileName);

                linea = sr.ReadLine();
                y_Height = Convert.ToInt32(linea);

                linea = sr.ReadLine();
                x_Widht = Convert.ToInt32(linea);

                generatedImage_bpm = new Bitmap(x_Widht, y_Height);


                for(int y=0; y < y_Height; y++)
                {
                    
                    for (int x=0; x < x_Widht; x++)
                    {
                        linea = sr.ReadLine();
                        if (linea == null)
                        {
                            break;
                        }
                        argb_segments = linea.Split(delimitador);

                        int a = Convert.ToInt32(argb_segments[0]);
                        int r = Convert.ToInt32(argb_segments[1]);
                        int g = Convert.ToInt32(argb_segments[2]);
                        int b = Convert.ToInt32(argb_segments[3]);

                        //SIEMPRE VA PRIMERO ALTURA LUEGO ANCHO
                        generatedImage_bpm.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                        Console.WriteLine("A: " + argb_segments[0] + " R: " + argb_segments[1] + " G: " + argb_segments[2] + " B: " + argb_segments[3]);



                    }

                    if (linea == null)
                    {
                        break;
                    }
                }


               
                Console.WriteLine("height: " + y_Height + " |Width: " + x_Widht);
                pictureBox3.Image = generatedImage_bpm;
                MessageBox.Show("Imagen Generada :)");
                sr.Close();


            }

        }

        private void bt_Caliz_Click(object sender, EventArgs e)
        {
            TextWriter escribir = new StreamWriter("D:\\Modular\\Imagen\\IMAGE DATA\\caliz.txt");
         
            for(int y=0; y < 10; y++)
            {
                for(int x=0; x<10; x++)
                {
                    escribir.WriteLine(x+" ");
                }
                escribir.WriteLine("\n");
            }

            escribir.Close();
        }
    }
}
