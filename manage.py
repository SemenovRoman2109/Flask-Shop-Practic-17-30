import project

def main():
    try:
        project.migrate()
        project.project.run(debug=True)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()