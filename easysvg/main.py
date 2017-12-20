import easysvg

def main():
    svg = easysvg.SvgGenerator()
    svg.begin(640, 480)

    svg.text('This is text', 20, 100)
    svg.circle(320, 360, 100, '#ff0000')

    svg.end()
    svg_string = svg.get_svg()
    print(svg_string)

if __name__ == "__main__":
    main()

