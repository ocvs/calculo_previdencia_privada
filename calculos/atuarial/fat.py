from calculos.atuarial.tabuas_qx import qx_dict


class FAT:
    def __init__(self, tabua='AT2000_NS', sexo='M', sexo_benef='F', juros_tabua=0.00):
        """

        :param tabua:
        :param sexo:
        :param sexo_benef:
        :param juros_tabua:
        """
        self.tabua = tabua
        self.juros_tabua = juros_tabua
        self.ax = self.fA_x_y(sexo)
        # self.ay = self.fA_x_y(sexo_benef)

    def fA_x_y(self, sexo):
        Dx = []
        lx = [1000000]
        Nx = []

        ax = []
        qx = qx_dict['_'.join([self.tabua, sexo])]['qx']
        # calcula   lx   e    Dx
        for i in range(120):
            lx.append(lx[i] * (1 - qx[i]))
            Dx.append(lx[i] * ((1 + self.juros_tabua) ** -i))

        # calcula Nx
        for i in range(120):
            Nx.append(sum(Dx[i:]))

        # calcula ax
        for i in range(120):
            if Dx[i] > 0:
                ax.append(12 * (Nx[i + 1] / Dx[i] + 11 / 24))

        self.Dx = tuple(Dx)
        self.Nx = tuple(Nx)
        return tuple(ax)

    def gar(self, prazo_renda, idade_saida_anos, juros_tabua):
        # vg = (Math.pow((1 + juros), (-MV.prazo)) - 1) / (1 - Math.pow(1 + juros, (1 / 12)));
        vg = prazo_renda * 12 if juros_tabua == 0 else (((1 + juros_tabua) ** -prazo_renda) - 1) / (
                    1 - ((1 + juros_tabua) ** (1 / 12)))

        fator_renda_garantida = vg + 12 * ((self.Dx[idade_saida_anos + prazo_renda] / self.Dx[idade_saida_anos]) * (
                self.Nx[idade_saida_anos + prazo_renda + 1] / self.Dx[idade_saida_anos + prazo_renda] + 11 / 24))

        # fatGar = vg + 12 * ((Dx[MV.IdSaidaA + (MV.prazo)] / Dx[MV.IdSaidaA]) * (
        #            (Nx[MV.IdSaidaA + (MV.prazo) + 1]) / Dx[MV.IdSaidaA + (MV.prazo)] + 11 / 24));
        return fator_renda_garantida

    def temp(self, prazo_renda, idade_saida_anos):
        fator_renda_temporaria = 12 * (
                (self.Nx[idade_saida_anos + 1] - self.Nx[idade_saida_anos + prazo_renda + 1]) / self.Dx[
            idade_saida_anos] + (11 / 24) * (1 - (self.Dx[idade_saida_anos + prazo_renda] / self.Dx[idade_saida_anos])))
        # fatTemp = 12 * ((Nx[MV.IdSaidaA + 1] - Nx[MV.IdSaidaA + MV.prazo + 1]) / Dx[MV.IdSaidaA] + (11 / 24) * (
        #           1 - (Dx[MV.IdSaidaA + MV.prazo] / Dx[MV.IdSaidaA])));
        return fator_renda_temporaria
