def taumBday(b, w, bc, wc, z):
    # Write your code here

    cost_b = min(bc, wc+z)
    cost_w = min(wc, bc+z)

    return b*cost_b + w*cost_w
