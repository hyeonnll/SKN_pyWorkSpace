# 선거 시스템
# - 유권자들이 후보자 기호(1~N)로 투표
# - 투표 결과를 리스트에 저장하고 집계하여 당선자(최다 득표자)를 출력

from typing import Dict, List, Tuple


def read_vote_input(voter_index: int, num_candidates: int) -> int:
    """유권자 한 명의 투표를 입력받아 유효한 기호 번호를 반환한다.

    잘못된 입력(정수 아님, 범위 벗어남)은 재입력을 요구한다.
    """
    while True:
        raw = input(f"{voter_index}번째 유권자, 후보 번호(1~{num_candidates})를 입력하세요: ")
        try:
            number = int(raw)
        except ValueError:
            print("정수를 입력하세요.")
            continue

        if 1 <= number <= num_candidates:
            return number
        print(f"1부터 {num_candidates} 사이의 번호만 입력 가능합니다.")


def tally_votes(votes: List[int], num_candidates: int) -> Dict[int, int]:
    """투표 리스트를 집계하여 후보 기호별 득표수를 반환한다."""
    results: Dict[int, int] = {i: 0 for i in range(1, num_candidates + 1)}
    for number in votes:
        if 1 <= number <= num_candidates:
            results[number] += 1
    return results


def find_winners(results: Dict[int, int]) -> Tuple[List[int], int]:
    """최다 득표 후보 기호 목록과 그 득표수를 반환한다. 동점 허용."""
    if not results:
        return [], 0
    max_votes = max(results.values())
    winners = [num for num, cnt in results.items() if cnt == max_votes]
    return winners, max_votes


def main() -> None:
    candidate = ["홍길동", "이순신", "강감찬", "율곡", "신사임당"]
    vote: List[int] = []  # 투표 번호 저장 리스트
    count = 10  # 유권자 수

    print("[후보자 목록]")
    for idx, name in enumerate(candidate, start=1):
        print(f"  {idx}. {name}")
    print()

    # 투표 진행
    for i in range(1, count + 1):
        number = read_vote_input(i, len(candidate))
        vote.append(number)

    # 집계
    results = tally_votes(vote, len(candidate))

    # 후보자별 출력
    print("\n[득표 결과]")
    for num in range(1, len(candidate) + 1):
        name = candidate[num - 1]
        print(f"  {num}. {name}: {results.get(num, 0)}표")

    # 당선자 계산
    winners, max_votes = find_winners(results)
    if not winners:
        print("\n투표 결과가 없습니다.")
        return

    # 동점 처리
    winner_names = ", ".join(candidate[num - 1] for num in winners)
    if len(winners) == 1:
        print(f"\n당선자: {winner_names} ({max_votes}표)")
    else:
        print(f"\n공동 당선: {winner_names} (각 {max_votes}표)")


if __name__ == "__main__":
    main()


