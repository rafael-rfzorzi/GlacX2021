

class CadEmpresa():
     def carrega_empresa(self):
        cod_emp = self.entradaCod_emp.get()

        self.entradaNome_emp.delete(0, END)
        self.entradaEndereco_emp.delete(0, END)
        self.entradaBairro_emp.delete(0, END)
        self.entradaMunicipio_emp.delete(0, END)
        self.entradaUf_emp.delete(0, END)
        self.entradaFone_emp.delete(0, END)
        self.entradaCep_emp.delete(0, END)
        self.entradaCpf_emp.delete(0, END)
        self.entradaRg_emp.delete(0, END)
        self.entradaObs_emp.delete(0, END)

        self.entradaNome_emp.insert(END, self.NomeEmpresa)
        self.entradaEndereco_emp.insert(END, self.NomeRuaEmp)
        self.entradaBairro_emp.insert(END, self.NomeBairroEmp)
        self.entradaMunicipio_emp.insert(END, self.MunicipioEmp)
        self.entradaFone_emp.insert(END, self.TelefoneEmp)
        self.entradaCpf_emp.insert(END, self.LicencaCpf)
        self.entradaObs_emp.insert(END, self.Licenca)
