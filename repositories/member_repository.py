from db.run_sql import run_sql
from models.member import Member
import repositories.membership_repository as membership_repo

def save(member):
    sql = "INSERT INTO members (first_name, last_name, membership_id) VALUES ( ?, ?, ? ) RETURNING id"
    values = [member.first_name, member.last_name, member.membership.id]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        membership = membership_repo.select(result['membership_id'])
        member = Member(result['first_name'], result['last_name'], membership, result['id'])
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership_id'], row['id'])
        members.append(member)
    return members

def update(member):
    sql = "UPDATE members SET (first_name, last_name) = (?, ?) WHERE id = ?"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)