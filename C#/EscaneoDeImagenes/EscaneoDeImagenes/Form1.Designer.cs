namespace EscaneoDeImagenes
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.bt_Importar = new System.Windows.Forms.Button();
            this.bt_Scan = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_GetPixel = new System.Windows.Forms.Button();
            this.bt_Caliz = new System.Windows.Forms.Button();
            this.bt_WriteData = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.btGenerateFromData = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            this.bt_GenerateFromARGB = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_Importar
            // 
            this.bt_Importar.Location = new System.Drawing.Point(24, 30);
            this.bt_Importar.Name = "bt_Importar";
            this.bt_Importar.Size = new System.Drawing.Size(86, 23);
            this.bt_Importar.TabIndex = 0;
            this.bt_Importar.Text = "Importar";
            this.bt_Importar.UseVisualStyleBackColor = true;
            this.bt_Importar.Click += new System.EventHandler(this.bt_Importar_Click);
            // 
            // bt_Scan
            // 
            this.bt_Scan.Enabled = false;
            this.bt_Scan.Location = new System.Drawing.Point(225, 73);
            this.bt_Scan.Name = "bt_Scan";
            this.bt_Scan.Size = new System.Drawing.Size(165, 23);
            this.bt_Scan.TabIndex = 1;
            this.bt_Scan.Text = "Escribir Byte Array";
            this.bt_Scan.UseVisualStyleBackColor = true;
            this.bt_Scan.Click += new System.EventHandler(this.bt_Scan_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox1.Location = new System.Drawing.Point(24, 165);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(405, 305);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // bt_GetPixel
            // 
            this.bt_GetPixel.Enabled = false;
            this.bt_GetPixel.Location = new System.Drawing.Point(413, 73);
            this.bt_GetPixel.Name = "bt_GetPixel";
            this.bt_GetPixel.Size = new System.Drawing.Size(181, 23);
            this.bt_GetPixel.TabIndex = 3;
            this.bt_GetPixel.Text = "GetPixel IN CONSOLE";
            this.bt_GetPixel.UseVisualStyleBackColor = true;
            this.bt_GetPixel.Click += new System.EventHandler(this.bt_GetPixel_Click);
            // 
            // bt_Caliz
            // 
            this.bt_Caliz.Location = new System.Drawing.Point(1363, 30);
            this.bt_Caliz.Name = "bt_Caliz";
            this.bt_Caliz.Size = new System.Drawing.Size(183, 23);
            this.bt_Caliz.TabIndex = 4;
            this.bt_Caliz.Text = "escribir random";
            this.bt_Caliz.UseVisualStyleBackColor = true;
            this.bt_Caliz.Click += new System.EventHandler(this.bt_Caliz_Click);
            // 
            // bt_WriteData
            // 
            this.bt_WriteData.Enabled = false;
            this.bt_WriteData.Location = new System.Drawing.Point(24, 73);
            this.bt_WriteData.Name = "bt_WriteData";
            this.bt_WriteData.Size = new System.Drawing.Size(159, 23);
            this.bt_WriteData.TabIndex = 5;
            this.bt_WriteData.Text = "Escribir DATA PIXEL";
            this.bt_WriteData.UseVisualStyleBackColor = true;
            this.bt_WriteData.Click += new System.EventHandler(this.bt_WriteData_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.SystemColors.AppWorkspace;
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox2.Location = new System.Drawing.Point(545, 165);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(417, 305);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox2.TabIndex = 6;
            this.pictureBox2.TabStop = false;
            // 
            // btGenerateFromData
            // 
            this.btGenerateFromData.Location = new System.Drawing.Point(665, 486);
            this.btGenerateFromData.Name = "btGenerateFromData";
            this.btGenerateFromData.Size = new System.Drawing.Size(162, 33);
            this.btGenerateFromData.TabIndex = 7;
            this.btGenerateFromData.Text = "Generar Imagen";
            this.btGenerateFromData.UseVisualStyleBackColor = true;
            this.btGenerateFromData.Click += new System.EventHandler(this.btGenerateFromData_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.label1.Location = new System.Drawing.Point(133, 142);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(121, 17);
            this.label1.TabIndex = 8;
            this.label1.Text = "Imagen Importada";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.label2.Location = new System.Drawing.Point(623, 142);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(303, 17);
            this.label2.TabIndex = 9;
            this.label2.Text = "Imagen generada desde un Byte Array en TXT";
            // 
            // pictureBox3
            // 
            this.pictureBox3.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.pictureBox3.Location = new System.Drawing.Point(1069, 165);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(438, 305);
            this.pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox3.TabIndex = 10;
            this.pictureBox3.TabStop = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.label3.Location = new System.Drawing.Point(1114, 142);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(348, 17);
            this.label3.TabIndex = 11;
            this.label3.Text = "Imagen generada desde un arreglo ARGB desde TXT";
            // 
            // bt_GenerateFromARGB
            // 
            this.bt_GenerateFromARGB.Location = new System.Drawing.Point(1208, 486);
            this.bt_GenerateFromARGB.Name = "bt_GenerateFromARGB";
            this.bt_GenerateFromARGB.Size = new System.Drawing.Size(163, 33);
            this.bt_GenerateFromARGB.TabIndex = 12;
            this.bt_GenerateFromARGB.Text = "Generar Imagen";
            this.bt_GenerateFromARGB.UseVisualStyleBackColor = true;
            this.bt_GenerateFromARGB.Click += new System.EventHandler(this.bt_GenerateFromARGB_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1689, 635);
            this.Controls.Add(this.bt_GenerateFromARGB);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btGenerateFromData);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.bt_WriteData);
            this.Controls.Add(this.bt_Caliz);
            this.Controls.Add(this.bt_GetPixel);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_Scan);
            this.Controls.Add(this.bt_Importar);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_Importar;
        private System.Windows.Forms.Button bt_Scan;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_GetPixel;
        private System.Windows.Forms.Button bt_Caliz;
        private System.Windows.Forms.Button bt_WriteData;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button btGenerateFromData;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button bt_GenerateFromARGB;
    }
}

