<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0613.txt",
      "sha256": "6b7d21a72894c2cbc04c923e8f2df6f3a87c218d294cd28b4f103995d285465a",
      "bytes": 12975
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "266200b1c6c00f14d8427b2dd1e8e2df675e5198b31047e4a4fbb33e8229a8bb",
      "bytes": 2414
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "269a77c75beda59fcdea023ba8ba2a183d9002d1059ee067cf20d4728d31a8c5",
      "bytes": 190505
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "94a6eaa8dfe334a120def08ff701e693dea3676faa7d25c4c2d6597556bd3081",
      "bytes": 770
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "8af013052de5789b45d7e654c2ba0d9c8b3c6b86fc686890f0c0bbbf6fcad53b",
      "bytes": 1774
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f387135157e9c937e8905e9cf6a3698ee64fa1e12401e07e74d802d6f1ea780e",
      "bytes": 1761
    },
    {
      "path": "characters/Jin-ho.md",
      "sha256": "073d8896aacde1d55ec5216b7fbb77cd3707164cd06698e16c3e80b54a08e694",
      "bytes": 565
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d430c777de2f96918feb064a61931da36d2088b1b04fed1c164c1c336c254530",
      "bytes": 622
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "4fdbafb793f08d1610f8d5fd902e93fea62f54e6318c5fb76e0eb6626f313df2",
      "bytes": 939
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "499f55c373ee05ad5c21baf50ef08cca4a8e12978e7713017b67a25ea1cac4a3",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5ca8d5386badc24a2a892157b6e8bd3785965bbe325211c453de8deaa76dca24",
      "bytes": 191819
    }
  ],
  "estimated_tokens": 10705
}
-->

# Durable State Update — Chapter 613

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 613. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 613. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 613,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 613,
    "continuity_sources": [613],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Al Diab Jawahiri, the leader of Al-Qaeda, remains in the Skeleton King's custody.",
    "The Skeleton King is an undead named monster who has fought alongside Jin Taekyung and is accepted by Chuck Hagel as an ally.",
    "Al-Qaeda possesses a large Magic Gem research laboratory that appears to have operated for at least ten years.",
    "Choi and Magic Johnson are investigating the Al-Qaeda laboratory and its research results.",
    "Restricted supplies found among the terrorists indicate that someone is supporting or supplying them from within established military, political, or smuggling networks.",
    "The masked group has destroyed terrorist leadership and headquarters while concealing its identities, creating a significant deterrent against further terrorist action.",
    "Middle Eastern terrorist groups and Afghan rebels have issued a joint statement promising restraint after the masked group's campaign.",
    "Jin-ho, now a civil servant in the Hunter and Gate Management Department, has inferred Jin Taekyung's involvement in the masked group's campaign and agreed to keep it secret.",
    "Jin Taekyung's training to complete a new martial result is in its final stage but is obstructed by the heart demon and grief over Kim Hwajong.",
    "Jin Taekyung intends to return to the Murim after recognizing that his reunion with Jin-ho provided the comfort and clarity he needed."
  ],
  "continuity_sources": [
    612
  ],
  "open_questions": [
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "Will the terrorist groups' apparent surrender and restraint last beyond the immediate pressure of the masked group's campaign?",
    "Can Jin Taekyung complete his training and overcome the heart demon?"
  ],
  "safe_through": 612,
  "temporary_decisions": [
    "Use Al Diab Jawahiri as the full English rendering of 알 디아브 자와히리.",
    "Retain Crazy Korean as Chuck Hagel's address for the masked protagonist.",
    "Preserve Jin-ho hyung as Jin-ho's familiar address.",
    "Render 심마 as heart demon.",
    "Keep Magic Gem laboratory for 마정석 관련 비밀 실험실."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 주화입마   | **qi deviation**                                 |                                                       |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 임꺽정 | **Im Kkeokjeong** |
| 진호 | **Jin-ho** | Jin Taekyung's older male friend, addressed as Jin-ho hyung. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소격변 | **Small Cataclysm** | Name given to the Sichuan Province monster wave. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 진호 | 태경 | Older male friend addressing a younger male friend in a close hyung relationship | Taekyung | Informal and familiar | Jin-ho addresses Taekyung as 태경아 in recalled advice; Taekyung refers to him as Jin-ho hyung. |
| 백한성 | 최민우 | President_to_trusted_political_ally | Team Leader Choi | formal-polite, warm, and politically attentive | Baek addresses Choi as 최 팀장님 during the private Blue House breakfast. |
| 최민우 | 백한성 | political_subordinate_to_President | Mr. President | formal-polite | Choi addresses Baek as 대통령님 during the breakfast and departure. |
| 진태경 | 진호 | younger_friend_to_older_friend | Jin-ho hyung | informal and familiar | Taekyung repeatedly addresses Jin-ho as hyung while joking, asking favors, and sharing personal concerns. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 603
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 597
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 612
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license; his Middle Dantian is partially activated at 10%, slightly improving the efficiency of his martial arts and internal energy.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jin-ho.md

# Jin-ho (진호)

- **Safe through:** Chapter 612
- **Aliases:** None
- **Role:** A civil servant in the Hunter and Gate Management Department and Jin Taekyung's older friend.
- **Personality:** Blunt, vulgar, perceptive, and good-natured beneath his teasing.
- **Voice:** Casual, profane, teasing, and irreverent.
- **Relationships:** Jin-ho is Jin Taekyung's older friend and trusted confidant; he has inferred Taekyung's involvement in the masked group's campaign and agrees to keep it secret.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 612
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 597
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 603
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and the current Guild Master of the Peace Guild and Vice Guild Master of Ares Guild after a unanimous board vote.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃613화



오늘도 트레이닝 룸은 적막했다.

바닥에는 수많은 종류의 병장기가 널브러져 있었고, 자동 복구 마법이 걸린 벽은 처참하게 무너진 상태였다.

그리고 그 중심에…… 가부좌를 튼 채 상념에 빠져 있는 내가 있다.

‘더. 아주 조금만 더.’

거의 다 왔다.

이 커다란 퍼즐의 마지막 한 조각.

진호 형과 헤어진 직후, 곧장 트레이닝 룸으로 처박힌 나는 그 한 조각을 위한 마지막 작업에 돌입해 있었다.

스트레스로 머리카락이 죄다 빠진다 해도, 설령 최악의 상황으로 치달아 주화입마의 위기가 온다 해도 이겨 내야 한다.

나는 무슨 수를 써서라도 떠나기 전 이 퍼즐을 완성해야 했다.

‘앞으로의 미래를 위해서.’

퍼즐의 마지막 조각을 찾기 시작한 것은 최근의 일이지만, 퍼즐을 맞춰야겠다고 생각한 것은 몇 달 전부터였다.

그래, 아마 소격변(小激變)이라 명명된 아크 리치와의 전투 이후였을 것이다.

‘이대로라면 모두가 위험하다.’

어느 날 불현듯 떠오른 생각.

그리고 시간이 흐름에 따라 불안감은 확신으로 변했다.

마력 수치는 비정상적으로 상승했고, 그에 따라 몬스터는 강력해졌으며, 대격변 이후 몰라볼 만큼 줄어들었던 인명 피해가 곳곳에서 속출했다.

지금의 현대 인류에게는 또 다른 힘이 필요했고, 나는 고민 끝에 결심했다.

무공(武功)을 창안(創案)하기로.

매일같이 불어나는 위험과 재앙에 맞서, 이들에게 새로운 검과 방패를 나누어 주기로.

물론 결코 쉬운 일은 아니었다. 최하급 헌터라도 익힐 수 있을 만한 안정성이 있는 동시에, 악인들에게 악용되지 않을 만큼의 적당한 위력을 지녀야 했으니까.

하지만…… 마침내 나는 이 거대한 퍼즐의 마지막 한 조각을 찾아냈다.

‘그래, 이거다.’

수백 번의 시도 끝에 완성시킨 하나의 길.

아직 이름을 붙이지 않은 심법(心法)을 완성시킨 그 순간.

띠링. 띠링. 띠링.

내 성공을 축하하듯, 힘찬 알림이 터져나왔다.



* * *



최 팀장, 아니 이제는 평화 길드장이자 아레스 길드의 부길드장으로 취임한 최민우는 그야말로 눈코 뜰 새 없이 바빴다.

일주일간 자리를 비운 사이 처리해야 할 안건은 수백 개로 불어나 있었고, 임시로 배정된 개인 비서는 사방에서 빗발치는 거물들의 전화에 진땀을 흘렸다.

“기, 길드장님. 청와대에서 오찬 일정 제의가 들어왔습니다.”

“정계와 전경련에서 친목회에 참석해 주십사 하는…….”

“길드 연합 측에서 게이트 관련 사업 연계 제안을…….”

“해외 지사 설립 건에 관하여…….”

거절할 수 없는 제안도, 충분히 거절할 수 있는 제안도 있었으나 최민우의 대답은 항상 같았다.

“알겠습니다. 일정 잡으세요.”

최민우는 분 단위로 짜인 스케줄에 맞춰 움직였다. 일하는 기계처럼 하루하루를 보내는 그는 잠도 제대로 자지 않았다.

위태로워 보일 만큼 바쁜 그의 모습에 주위 사람들은 우려 섞인 시선을 보냈다.

“자, 하나만 선택해요. 최 팀장님. 최 길드장님. 최 부길드장님. 이 셋 중에 어떤 호칭으로 불러 드릴까요?”

“팀장님이라고 불러 주십시오. 우린 그때 만났으니까요.”

“좋아요. 그럼 최 팀장님. 단도직입적으로 말하겠는데…… 좀 쉬어요. 스케줄 좀 줄이고, 자잘한 업무는 비서에게 맡기라고요.”

“맞아, 최 팀장. 아무리 젊다지만 계속 이러다간 자네가 힘들어져.”

“저는 괜찮습니다. 두 분 다 걱정하지 마세요.”

“최 팀장님.”

“아니, 그러지 말고…….”

“괜찮습니다, 저는.”

담담한 목소리로 똑같은 대답을 반복하는 최민우의 모습에, 그를 만류하려던 송송이와 임꺽정도 입을 다물 수밖에 없었다.

하지만 어째서일까. 그들의 귀로 흘러들어온 대답은 처음과 같았지만, 마음속으로 전해진 대답은 처음과 달랐다.

괜찮습니다, 저는.

같으면서도 다른 그 한 마디를 남긴 최민우는 계속해서 일에 파묻혔다.

그나마 곁에서 약간의 도움을 주던 개인 비서마저 떠나보낸 채, 더욱 바빠진 일상 속에서 정신없이 시간을 보냈다.

어느 날 가진 백한성 대통령과의 독대에서 그에 관한 대화가 오간 것도 결코 이상한 일이 아니었다.

“요새 많이 바빠 보이시는군요.”

“그래서 좋습니다.”

“듣자 하니 이제는 비서도 두지 않으신다던데…… 무슨 특별한 이유라도 있으십니까?”

“커피.”

“예?”

“커피를 못 타더군요. 그뿐입니다.”

백한성 대통령은 농담이라 생각하고 웃어넘겼지만, 최민우가 그에게 했던 대답은 모두 진심이었다.

최민우는 정신없이 일에 파묻힌 지금이 좋았고, 젊은 비서가 타 주던 커피는 희한할 만큼 맛이 없었다.

그리고…… 자꾸만 머릿속에 떠오르는 누군가에 대한 그리움과 슬픔을 이렇게나마 잠시 잊을 수 있음에 감사했다.

“잠시 실없는 이야기를 했습니다. 다음 안건으로 넘어가시죠.”

하루. 또 하루.

진태경이 고립된 공간에서 수련을 거듭했다면, 최민우는 수많은 사람을 만나는 와중에도 스스로를 고립시켰다.

아마 그래서였을지도 모른다. 어느 날 문득 한 사람이 이름이 생각난 것은.

여느 때처럼 가혹하리만치 자신을 몰아붙이던 그 날, 마음 깊숙한 곳에 억누르고 있던 그리움이 고개를 든 것은.

“정 기사님, 차 돌리십시오.”

“예? 죄송하지만 제가 알기로는 다음 스케줄 장소가…….”

“오늘 일정은 전부 캔슬입니다. 가야 할 곳이 있어요.”

백미러를 통해 마주친 운전기사의 당황한 눈빛을 뒤로한 채 최민우는 리무진 시트 깊숙이 몸을 파묻었다.

반쯤 열린 창문 사이로 스며드는 따뜻한 봄바람과 햇빛을 받으며, 한 사람을 만나기 위한 장소로 향했다.

저벅. 저벅.

홀로 오른 언덕은 높으면서도 가팔랐고, 최민우의 발걸음은 무거웠다. 아니, 어쩌면 무거운 것은 그의 마음이었을 것이다.

높고 가파른 이 길을 백 번, 천 번을 오른다 해도 닿을 수 없는 한 사람에 대한 슬픔과 죄책감이 최민우의 마음을 짓눌렀다.

툭. 투둑.

가는 길에 이른 꽃망울을 틔운 봄꽃을 한 아름 땄다. 새하얀 제비꽃으로도 부족한 것 같아, 길을 따라 모여 있는 선홍빛 꽃잔디도 섞였다.

이제는 곁에 없는 그는 언제나 붉은색을 좋아했다고 했다.

‘그런데도 늘 검은색 정장을 입으셨었지.’

불과 얼마 전에야 알았다. 그가 가장 좋아하는 색이 무엇이었는지. 그 많던 바이크는 왜 팔았는지.

어째서 그토록 가까이하던 술을 끊고, 덥수룩하게 길렀던 수염과 장발을 정돈하여 깔끔하게 가르마를 탔는지.

‘왜 그러셨습니까. 제게는 당신만으로 충분했는데.’

모든 걸 알게 되었지만, 모든 것이 늦어 버렸다.

최민우는 욱신거리는 가슴을 느끼며 그렇게 걸었다.

따뜻하고 바람 잘 드는 언덕 위에는 커다란 봉분(封墳)이 그를 기다리고 있었고, 화강암을 깎아 만든 비석에 새겨진 세 글자는 유난히도 선명했다.

故김 화 종.

무슨 말을 해야 할까. 차가운 설산이 아닌, 따스한 언덕에 잠든 노집사를 멍하니 바라보던 최민우의 입술이 열렸다.

“저 왔습니다.”

언제나 침착하던 눈동자가 파르르 떨렸다. 떨림이 전해진 입술을 꽉 깨문 최민우가 천천히 말을 이었다.

“……할아버지.”

마음에만 품은 채 생전 단 한 번도 건네지 못한 그 한 마디가 흘러나온 그때.

솨아아아.

어디선가 불어온 바람이 최민우의 전신을 휩쓸었다. 언덕에 깔린 잔디가 허리를 굽히고 나뭇가지가 손을 흔들었다.

그리고 다음 순간, 손에 든 꽃다발을 봉분 옆에 내려놓은 최민우의 몸이 우뚝 굳었다.

‘저건.’

의문과 함께 커지는 눈동자. 그의 시선이 멈춘 곳은 비석의 뒷면이었다.

지금까지 미처 발견하지 못했던 그곳에는 또 다른 글씨가 새겨져 있었다.



왔구나.

고맙고, 사랑한다.

행복해라.



“……!”

누가 새겨 놓은 글귀였을까. 당연히 들었어야 할 의문이었지만 지금만큼은 상관없었다.

최민우는 석상처럼 굳은 채, 하염없이 그 짧은 문장을 바라보았다.

바람에 흔들리는 꽃처럼 그의 마음도 흔들리고 있었다. 가슴 깊숙한 어디에선가 불쑥 솟구친 무언가가 목을 틀어막고 눈동자를 뜨겁게 달구었다.

“아.”

그저 모든 것이 먹먹해져, 목맨 탄식을 토해 낸 그 순간이었다.

“빨리 왔군. 최소한 며칠은 더 기다려야 할 줄 알았는데.”

불쑥 들려온 누군가의 목소리.

돌아선 최민우의 시야에, 작은 상자를 든 채 서 있는 한 사람의 모습이 비쳤다. 스켈레톤 킹이었다.

왜 그가 이곳에 있는 것일까. 기다렸다는 말은 무슨 뜻일까.

그러나 그런 의문은 떠오름과 동시에 사라졌다.

지금의 최민우에게 필요한 건 이유가 아닌 온기였으니까. 스스로 답을 찾을 수 없는 문제에 관한 대답이었으니까.

“하나만, 한 가지만 물어봐도 되겠습니까.”

평소의 스켈레톤 킹이었다면 퉁명스럽게 안 된다고 대답했을 것이다.

그러나 이번에는 아니었다. 그는 선선히 고개를 끄덕였다.

“뭐든.”

“만약 진태경 씨였다면…… 이럴 때 어떻게 했을까요?”

갑작스러운 질문이었으나 스켈레톤 킹은 즉각 그 말의 의미를 깨달았다.

“그건 왜 묻지?”

“그는 내가 아는 사람 중, 누구보다 강한 사람이니까.”

말없이 최민우를 응시하던 스켈레톤 킹이 나직한 목소리로 대답했다.

“울었을 거다. 틀림없이.”

“……!”

“그리고 극복하고 계속해서 살아가겠지. 떠난 사람을 영원히 기억하면서.”

그것만으로도 충분했다.

최민우는 참았던 눈물을 흘렸다. 슬픔과 후회. 그리움과 죄책감을 눈물과 함께 흘려보냈다.

그리고 스켈레톤 킹은 조용히 물러나며 생각했다.

이 상자에 담긴 물건들은, 잠시 후에 전해 주는 것이 좋겠다고.

동시에 반나절 전쯤 자신에게 이것을 맡기며 진태경이 했던 말을 떠올렸다.



‘미안한데, 부탁 하나만 하자.’

‘싫다. 안 된다. 돌아가라.’

‘이걸 최 팀장님한테 전해 줘. 그 외에는 누구도 안 돼.’

‘빌어먹을 인간 같으니. 이제는 들은 척도 안 하는군. 이 몸이 잔심부름꾼으로 보이나?’

‘잔심부름꾼이 아니라, 널 믿으니까 맡길 수 있는 거다.’

‘……전해 줘야 하는 게 도대체 뭔데?’

‘무공(武功).’

‘뭐?’

‘그렇게 말하면 알 거다. 상자 안에 편지 있으니까 꼭 읽어 보라고 하고.’

‘아니. 가뜩이나 요새 보이지도 않는 인간을 어떻게…….’

‘김 집사님 묘지에서 기다려. 그전에는 만나더라도 입 벙긋하지 말고. 아마 이겨 낼 시간이 필요할 거야.’



스켈레톤 킹의 생각에, 진태경은 아무리 생각해도 괴상한 인간이었다.

그의 말마따나 묘지에서 딱 마주친 것도 그렇고.

한 번 잠들면 멱살을 잡고 흔들어 깨워도 눈 하나 깜짝하지 않는다는 점에서 더더욱 그랬다.

‘망할. 감히 이 몸에게 고작 이따위 잔심부름을 시키고, 혼자서 맘 편히 잠을 자?’

절대 깨우지 말라며 신신당부까지 했으니 지금쯤이면 곯아떨어져 있을 것이다.

스켈레톤 킹은 그런 진태경을 생각할수록 괘씸했지만, 솔직히 말하자면 이상하리만치 기분이 썩 나쁘지 않았다.

‘널 믿으니까 맡긴다. 믿음이라, 음. 으음.’

자신이 들고 있는 상자와 진태경의 한 마디를 떠올리며 고개를 끄덕거리던 스켈레톤 킹이 작게 중얼거렸다.

“……좋은 꿈 꾸거라. 간악한 인간아.”

솨아아아.

다시 한번 바람이 분다. 한 사람의 흐느낌과 어느덧 사람과 가까워진 한 몬스터의 목소리가 바람에 파묻혔다.
```

## Final English reading copy

```markdown
# Chapter 613

The Training Room was silent again today.

Countless kinds of weapons lay strewn across the floor, and the walls—enchanted with automatic restoration magic—had been reduced to a miserable ruin.

And at the center of it all… there I was, sitting cross-legged and lost in thought.

*More. Just a little more.*

I was almost there.

The final piece of this enormous puzzle.

Immediately after parting ways with Jin-ho hyung, I had holed myself up in the Training Room and begun the final work required to find that last piece.

Even if stress made every hair on my head fall out, even if things reached the worst possible point and I faced the danger of qi deviation, I had to overcome it.

No matter what it took, I had to complete this puzzle before I left.

*For the future ahead.*

I had only begun looking for the puzzle’s final piece recently, but I had been thinking about putting the puzzle together for several months.

Yes. It had probably been after the battle with the Arch Lich—the incident dubbed the Small Cataclysm.

*If things continue like this, everyone will be in danger.*

It was a thought that had suddenly occurred to me one day.

And as time passed, my unease had turned into certainty.

Mana levels had risen abnormally, monsters had grown stronger accordingly, and human casualties—which had fallen dramatically after the Great Cataclysm—were once again mounting everywhere.

Modern humanity needed another kind of power, and after much thought, I made a decision.

To create martial arts.

To hand them a new sword and shield with which to face the dangers and disasters that grew every day.

Of course, it was anything but easy. The martial art had to be stable enough for even the lowest-rank Hunter to learn, while still possessing a moderate level of power that evil people could not easily abuse.

But… at last, I had found the final piece of this enormous puzzle.

*Yes. This is it.*

A single path completed after hundreds of attempts.

The moment I completed the cultivation technique I had not yet given a name.

Ding. Ding. Ding.

As if to congratulate me on my success, a series of vigorous alerts rang out.

* * *

Team Leader Choi—or rather, Choi Minwoo, who had now taken office as Guild Master of the Peace Guild and Vice Guild Master of Ares Guild—was so busy that he barely had time to breathe.

The matters requiring his attention had multiplied into the hundreds during the week he had been away, and his temporarily assigned personal secretary was sweating bullets as calls from bigwigs poured in from every direction.

“G-Guild Master. The Blue House has proposed a luncheon.”

“The political world and the Federation of Korean Industries would like you to attend a social gathering…”

“The Guild Alliance has proposed a partnership concerning Gate-related business…”

“Regarding the establishment of overseas branches…”

Some of the proposals could not be refused, while others could easily have been rejected. But Choi Minwoo’s answer was always the same.

“All right. Schedule them.”

Choi Minwoo moved according to a schedule planned down to the minute. He spent each day like a machine, barely sleeping at all.

The people around him watched his dangerously busy routine with concern.

“Now, choose one. Team Leader Choi, Guild Master Choi, or Vice Guild Master Choi. Which title should we use to address you?”

“Please call me Team Leader Choi. That was my title when we met.”

“All right, then. Team Leader Choi, I’ll be direct… Get some rest. Cut down your schedule and leave the minor tasks to your secretary.”

“She’s right, Team Leader Choi. You may be young, but if you keep going like this, you’ll wear yourself out.”

“I’m fine. Please don’t worry, either of you.”

“Team Leader Choi.”

“No, really…”

“As for me, I’m fine.”

Faced with Choi Minwoo calmly repeating the same answer, Song Song and Im Kkeokjeong, who had tried to dissuade him, could do nothing but fall silent.

And yet, why was it?

The answer that reached their ears was the same as before, but the answer that reached their hearts was different.

*As for me, I’m fine.*

Choi Minwoo left them with that one phrase, the same and yet different, and continued burying himself in work.

He even sent away the personal secretary who had been giving him a little help, then spent his days in a frenzy as his already hectic life grew even busier.

It was only natural that a conversation about him would come up one day during a private meeting with President Baek Hanseong.

“You seem very busy these days.”

“That’s why I like it.”

“I heard you no longer even keep a secretary… Is there some special reason?”

“Coffee.”

“Pardon?”

“She couldn’t make coffee. That’s all.”

President Baek Hanseong assumed it was a joke and laughed it off, but every answer Choi Minwoo had given him was sincere.

Choi Minwoo liked being buried in work so completely, and the coffee made by his young secretary had been strangely awful.

And… he was grateful that, at least for a little while, this allowed him to forget the longing and sadness he kept feeling for someone who repeatedly came to mind.

“I’ve wasted enough time on idle conversation. Let’s move on to the next item.”

One day. Then another.

While Jin Taekyung continued training in an isolated space, Choi Minwoo isolated himself even while meeting countless people.

Perhaps that was why, one day, he suddenly remembered someone’s name.

On that day, when he had been pushing himself with almost cruel intensity as usual, the longing he had been suppressing deep in his heart raised its head.

“Driver Jung, turn the car around.”

“Pardon? I’m sorry, but as far as I know, our next scheduled location is…”

“Cancel everything on today’s schedule. There’s somewhere I need to go.”

Leaving behind the driver’s startled gaze in the rearview mirror, Choi Minwoo sank deep into the limousine seat.

With the warm spring breeze and sunlight flowing through the half-open window, he headed toward a place where he could meet someone.

Step. Step.

The hill he climbed alone was high and steep, and Choi Minwoo’s footsteps were heavy.

No—perhaps it was his heart that was heavy.

Sorrow and guilt over the one person he could never reach, even if he climbed this high, steep path a hundred or a thousand times, weighed on Choi Minwoo’s heart.

Rustle. Pluck.

Along the way, he gathered an armful of spring flowers that had bloomed early. The pure white violets did not seem like enough, so he added the scarlet moss phlox growing in clusters along the path.

The man who was no longer by his side had always said he liked red.

*And yet he always wore black suits.*

It was only recently that Choi Minwoo had learned what color he liked most, and why he had sold all those motorcycles.

Why he had quit drinking despite once keeping alcohol so close, and why he had trimmed the shaggy beard and long hair he had grown out before neatly parting it.

*Why did you do that? You were enough for me.*

He had learned everything, but he had learned it all too late.

Feeling the dull ache in his chest, Choi Minwoo continued walking.

On the warm, breezy hilltop, a large burial mound awaited him, and the three characters carved into the granite gravestone stood out with unusual clarity.

**The late Kim Hwajong.**

What was he supposed to say?

Staring blankly at the old butler sleeping beneath the warm hill rather than a cold, snow-covered mountain, Choi Minwoo opened his mouth.

“I’m here.”

The eyes that had always remained calm trembled faintly. Choi Minwoo bit down hard on his trembling lips, then slowly continued.

“…Grandfather.”

The one word he had held in his heart but never once managed to say while the old man was alive finally slipped out.

Whoosh—

A wind that had come from somewhere swept over Choi Minwoo’s entire body. The grass covering the hill bowed at the waist, and the branches waved their hands.

Then, the next moment, Choi Minwoo set the bouquet beside the burial mound—and froze.

*What’s that?*

His eyes widened with puzzlement. His gaze had stopped on the back of the gravestone.

There, in a place he had failed to notice until now, other words had been carved.

> You came.
>
> Thank you, and I love you.
>
> Be happy.

“……!”

Who had carved those words?

It was an obvious question, but for the moment, it did not matter.

Choi Minwoo stood frozen like a stone statue, staring endlessly at the short message.

His heart trembled like flowers swaying in the wind. Something that had suddenly surged up from somewhere deep inside his chest blocked his throat and heated his eyes.

“Ah.”

Overwhelmed by it all, he let out a choked sigh.

“You came quickly. I thought I’d have to wait at least a few more days.”

Someone’s voice suddenly rang out.

Choi Minwoo turned around. In his field of vision stood someone holding a small box.

It was the Skeleton King.

Why was he here?

What did he mean by saying he had been waiting?

But those questions disappeared as soon as they arose.

What Choi Minwoo needed now was not a reason, but warmth.

He needed an answer to a question he could not answer on his own.

“May I ask just one thing? Just one question.”

Under normal circumstances, the Skeleton King would have bluntly said no.

But not this time.

He readily nodded.

“Anything.”

“If it had been Mr. Jin Taekyung… what would he have done at a time like this?”

It was a sudden question, but the Skeleton King immediately understood what it meant.

“Why do you ask?”

“Because he’s the strongest person I know. Stronger than anyone else.”

The Skeleton King stared at Choi Minwoo in silence before answering in a low voice.

“He would have cried. Without a doubt.”

“……!”

“And then he would overcome it and go on living, forever remembering the person who left.”

That was enough.

Choi Minwoo shed the tears he had been holding back. He let his sorrow and regret, his longing and guilt, flow away with them.

The Skeleton King quietly stepped back and thought that it would be better to hand over the things in the box a little later.

At the same time, he recalled what Jin Taekyung had said about half a day earlier when entrusting the box to him.

*“I’m sorry, but let me ask you one favor.”*

*“I don’t want to. No. Go back.”*

*“Give this to Team Leader Choi. No one else.”*

*“You damnable human. Now you’re not even pretending to listen. Do I look like an errand boy to you?”*

*“It’s not because you’re an errand boy. I can entrust it to you because I trust you.”*

*“…What exactly am I supposed to deliver?”*

*“Martial arts.”*

*“What?”*

*“He’ll understand if you put it that way. Tell him there’s a letter inside the box and make sure he reads it.”*

*“No. As if I could find a human I haven’t even seen lately…”*

*“Wait at Butler Kim’s grave. Even if you run into him before then, don’t say a word. He’ll probably need time to overcome it.”*

The Skeleton King thought that Jin Taekyung was an exceedingly strange human, no matter how much he considered it.

For one thing, he had run into Choi Minwoo at the cemetery exactly as Taekyung had predicted.

And he was even stranger for the fact that once he fell asleep, he would not so much as blink even if someone grabbed him by the collar and shook him awake.

*Damn him. How dare he make me run such a pathetic errand while he sleeps peacefully by himself?*

Jin Taekyung had repeatedly begged him not to wake him under any circumstances, so he was probably dead asleep by now.

The more the Skeleton King thought about Jin Taekyung, the more infuriating he found him. But honestly, for some strange reason, he did not feel all that bad.

*“I can entrust it to you because I trust you.” Trust, huh? Hmm. Hmmm.*

The Skeleton King nodded as he remembered the box in his hands and Jin Taekyung’s words, then muttered quietly.

“…Have a good dream, you devious human.”

Whoosh—

The wind blew once more.

One man’s sobs and the voice of a monster who had grown closer to humanity were swallowed by the wind.
```
