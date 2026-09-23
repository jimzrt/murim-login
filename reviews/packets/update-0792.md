<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0792.txt",
      "sha256": "3e26b2e81f3bea7a793745b594d9d5b77e3da4cd04a378e7ccaf33a6908aecdc",
      "bytes": 12816
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "301b1357e5643567cbced4c6d14501a3fcec7461ced4d7f1a1b57e1e48841df2",
      "bytes": 1267
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b107ad8b032275926005814226705b9c99fd04942849ff404275ebe5d6ff70cc",
      "bytes": 223952
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e98d83db26f72624a9b3013c040c64720e094aca40d0aaf8785e1ade8cab0d06",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "65a016e993b7b09dd73c15abff9b703f6e8555355809a2614d261df1955de0a1",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f1b372cd77e65a65d5d3d27eb706df54622251df6fd9a2969cfaf991720be4c8",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "5c5b550a99b36fbf1fa6a0e015d53eda65e1fb56a6d98505161acb334de072fb",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c1c9a1322aff96ba659e842af77d0c8eef5726cb081a364c1755d6eb6cb2e430",
      "bytes": 245359
    }
  ],
  "estimated_tokens": 9013
}
-->

# Durable State Update — Chapter 792

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 792. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 792. Profile updates may replace only one
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
  "chapter": 792,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 792,
    "continuity_sources": [792],
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
    "Jin Taekyung is the World Hunter Federation's Alliance Leader.",
    "The Main Quest [Cataclysm] requires Jin to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is hiding somewhere in the Middle East and possesses a large quantity of unrefined Magic Gems; Jin suspects they are preparing a major attack but are not ready yet.",
    "The World Hunter Federation and allied forces have deployed 100,000 Hunters to search for The Prophet; the search has found no notable leads after its first day, and the worst-case estimate exceeds sixty days.",
    "The Skeleton King and Xiao Shen are investigating a site where a search squad lost contact; the Skeleton King has spotted something unidentified."
  ],
  "continuity_sources": [
    790,
    791
  ],
  "open_questions": [
    "Can Jin find and eliminate The Prophet before the Main Quest's time limit expires?",
    "What is the unidentified thing the Skeleton King has spotted?",
    "When will The Prophet's attack begin, and what will the Cataclysm involve?"
  ],
  "safe_through": 791,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Do not identify what the Skeleton King spots until it is revealed."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 방장      | **Abbot**                                                       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 791
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 791
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 791
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 791
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃792화



“……저게 뭐지?”

그 말에 고개를 돌린 샤오 쉔은 어떤 이상한 점도 발견하지 못했지만, 스켈레톤 킹은 아니었다.

비록 매직 존슨의 환영 마법 덕분에 인간과 같은 모습을 하고 있다 해도, 그는 근본적으로 몬스터였으니까.

그것도 무려 최상위에 속한 언데드 몬스터.

그런 의미에서 지금 이 순간 스켈레톤 킹을 사로잡은 감각은, 그가 가진 힘의 원천(源泉)과 맞닿아 있는 무언가였다.

‘빌어먹을. 이건…….’

틀림없다.

흐릿하지만 분명히 느낄 수 있었다.

달빛조차 집어삼킨 어두운 하늘 아래, 끝없이 펼쳐진 사막 위로 흩어져 가는 죽음의 기운을.

단 한 방울의 핏자국도 시체도 보이지 않았지만, 스켈레톤 킹은 어둠 너머에서 자신의 본능을 자극하는 기운의 정체가 사기(死氣)라는 것을 깨달았다.

지금으로부터 약 한 시간 전, 갑작스럽게 연락이 두절된 수색대가 어떤 운명을 맞이했는지도.

“애송이 인간.”

“네?”

“곧장 본대에 연락해라. 수색대를 찾았다고.”

“……!”

어떠한 흔적도 보이지 않는 고요한 사막. 그러나 그와는 상반되는 스켈레톤 킹의 한마디.

그제야 뒤늦게 상황을 깨달은 샤오 쉔이 굳은 얼굴로 고개를 끄덕였고, 스켈레톤 킹은 본능을 따라 발걸음을 옮겼다.

사박. 사박.

사막에 찍히는 발자국과 허물어지는 모래알.

열 걸음 정도를 그렇게 걸었을까. 문득 제자리에 멈춰선 스켈레톤 킹이 작게 중얼거렸다.

“어떤 놈인지, 깊게도 파묻어 놨군.”

그리고 다음 순간.

화아아악.

망망대해처럼 펼쳐져 있던 사막의 일부가 허공으로 솟구쳤다.

단 한 번의 손짓과 함께 흘러나온 거대한 마력이 모래를 지탱했고, 그 아래에 숨겨져 있던 스무 구의 시신을 확인한 스켈레톤 킹은 자신도 모르게 움직임을 멈췄다.

“……!”

섬광처럼 뇌리를 스치는, 그리 오래되지 않은 최근의 기억.

그와 동시에 전신을 엄습하는 불길한 직감.

‘잠깐. 그렇다면 설마.’

그러나 스켈레톤 킹의 생각은 그리 길게 이어지지 못했다. 아니, 그럴 수 없었다.

솨아아아.

어디선가 불어온 서늘한 바람에 휩쓸려 흩날리는 모래알.

그리고 그 안에 스며 있는 무언가.

저 멀리 칠흑 같은 어둠에 잠긴 사막 어딘가를 응시하던 스켈레톤 킹은, 아직 아무것도 눈치채지 못한 샤오 쉔을 향해 물었다.

“본대에는, 연락했나?”

“네. 지금 곧바로 인근에서 대기 중인 지원팀을 보내겠다고 답신이 왔…….”

“예상 소요 시간은?”

“최대 30분으로 예상됩니다.”

“30분이라. 애매하군.”

작게 중얼거린 스켈레톤 킹이 입맛을 다셨다.

“누군가를 지키는 건 자신 없는데.”

“……?”

“흠.”

의아해하는 샤오 쉔을 위아래로 훑어본 스켈레톤 킹이 한숨을 내쉬었다.

“이봐, 애송이 인간. 지금부터 이 몸이 두 가지 임무를 줄 거야.”

“앗, 넵. 킹 선생님께서 시키시는 일이라면 뭐든 하겠습니다.”

“좋은 태도야. 그럼 일단은 네 녀석이 가진 그 빌어먹을 특수 무전기를 다시 꺼내서 본대에 전해.”

“뭐라고 전할까요?”

“최대한 빨리, 가장 쓸 만한 인간들을 이곳으로 보내라고. 거북이를 타고 오는 약해빠진 지원팀 말고. 알겠나?”

시신을 수습하는 일에 왜 그 정도의 신속함과 인력이 필요한지는 모르겠지만, 샤오 쉔은 별다른 망설임 없이 고개를 끄덕였다.

그가 세상에서 가장 존경하는 인물은 진태경이었고, 스켈레톤 킹은 바로 그 진태경의 친구였으니까.

“알겠습니다. 그럼 두 번째 임무는 뭡니까?”

하지만 뒤이어 들려온 대답에는, 그런 샤오 쉔조차 되묻지 않을 수 없었다.

“무기를 들어라.”

“네?”

“그리고 스스로를 지켜. 자신 없으면 도망쳐도 좋다.”

“자, 잠깐만요.”

이게 무슨 소리지?

그리고 이 종잡을 수 없는 임무에 눈을 깜빡이던 샤오 쉔은, 얼마 지나지 않아 스켈레톤 킹이 했던 말의 의미를 깨달을 수 있었다.

득. 드드득.

지면을 통해 전해지는, 정체를 알 수 없는 진동.

서서히 거세지는 진동을 따라 사방에서 튀어 오르는 무수한 모래알들과 그 순간 떠오른 짐작을 확신으로 굳혀 버리는 스켈레톤 킹의 한 마디까지.

“많이도 몰려왔군.”

“……!”

샤오 쉔은 대답하지 않았다.

멍하니 입을 벌린 채 저 멀리 펼쳐진 사막의 지평선(地平線)을 바라보는 그의 눈동자에, 살아 있는 생물처럼 꿈틀거리는 어둠이 비쳤다.

아니, 눈으로는 헤아릴 수 없을 만큼 수많은 몬스터가.

‘몬스터 웨이브(Monster Wave)……!’

그리고 인류의 악몽으로 자리 잡은 그 단어가 샤오 쉔의 머릿속을 강타한 그때.

사박.

스켈레톤 킹은 빠르게 가까워지는 괴물들의 파도를 향해 나아갔다.

그의 발걸음에는 어떤 두려움이나 망설임도 없었고, 넘실거리며 뻗어 나온 강대한 마력은 끝없이 뻗어 나갔다.

- 왕의 이름으로 명하니.

나직한 목소리가 사막을 울렸다. 짙은 어둠을 뚫고, 오랜 시간과 무수한 모래알에 짓눌려 있던 망령들을 일깨웠다.

- 부름에 답하라.

드드드득!

지진과도 같은 진동이 사막을 휩쓸었다.

죽음의 기운으로 가득한 왕의 부름에, 깊은 잠에서 깨어난 망령들이 모래를 뚫고 지상으로 솟구쳤다.

파스슥!

흩날리는 희뿌연 모래와 어둠 속에서도 번뜩이는 새하얀 백골들.

- 크르릉.

죽음 이후 아름다운 가죽을 잃어버린 아라비아 표범이 기지개를 켰고, 초록빛 안광(眼光)을 빛내는 늑대와 하이에나 무리의 머리 위로 힘차게 날아오른 수십 마리의 독수리가 뼈밖에 남지 않은 날개를 펼쳤다.

- 삐이이잇!

날카로운 울음소리가 밤하늘을 가른다. 수 미터에 이르는 거대한 날개를 펼친 독수리들은 드높은 상공을 유영했다.

지상에서 모래바람을 일으키며 돌격해 오는 몬스터 군단의 머리 위를 지나쳐, 드넓은 사막과 숲으로 흩어져 나아가는 독수리들에게 주어진 임무는 오직 하나뿐이었다.

바로 왕의 명령에 따라, 이곳에 없는 한 존재를 찾아내는 것.

- 이 사막 어딘가에 인간의 냄새가 밴 무언가가 있다. 찾아내. 반드시.

독수리들은 힘차게 날갯짓했다.

그들에게는 바람을 타고 나아갈 깃털 대신 마력이 있었고, 생기(生氣)를 잃었으나 마르지 않는 활력(活力)이 있었다.

쉬이이익!

그리고 까마득한 지상에서 멀리 사라져가는 독수리 무리를 바라보던 왕은, 조금 전 자신이 보았던 인간들의 시신을 생각하며 코앞까지 들이닥친 몬스터 군단을 향해 걸음을 옮겼다.

‘그건 도대체 무슨 흔적이었을까.’

후웅, 콰아아앙!

내뻗은 주먹 끝에서 발산된 거대한 마력이 선두의 몬스터들을 집어삼킨다.

동시에 텅 비어 버린 공백 사이로 파고든 백여 마리의 맹수들이 흉포하게 날뛰었다.

- 캬우우우!

뻐억!

표범이 휘두른 앞발에 오크의 상반신이 날아가고, 머리 위로 떨어져 내리는 곤봉을 민첩하게 피한 하이에나 무리가 트롤의 전신에 이빨을 박아넣는다.

콰득!

비교도 안 되는 수적 열세.

그러나 스켈레톤 킹은 전투의 시작과 함께 깨달았다.

미카엘 실베르트의 마력 중 일부를 흡수하며 더욱 강력해진 권능은, 한낱 맹수에 불과했던 망령들조차 평범한 몬스터 따위는 단숨에 짓이길 힘을 불어넣어 주었다는 것을.

퍼걱! 콰드드득!

- 크아아아!

피와 살이 튀고, 살아 있는 것들의 비명이 울려 퍼졌다.

삽시간에 허물어지기 시작하는 진형.

단 일격으로 세 마리의 오우거의 머리를 날려 버린 스켈레톤 킹은 어둠이 내려앉은 사막 어딘가를 바라보았다.

비록 아무것도 보이지 않지만, 그는 알고 있었다.

수색대를 죽인 알 수 없는 무언가는, 이미 이 자리를 떠나 저 사막 어딘가로 모습을 감추었다는 것을.

‘도대체, 네놈은 무엇이냐.’

하지만 마음속에 던진 물음은 어디에도 닿지 못했고, 깊게 가라앉은 눈빛으로 어둠 속을 응시하던 스켈레톤 킹은 썩은 통나무처럼 쓰러진 오우거를 죽음에서 일으켜 세웠다.

아니, 주위의 모든 것을.

- 부름에 답하라.

화아아악.

마력이라고는 믿을 수 없을 만큼 눈부신 금빛 광휘가 사방으로 퍼진다.

어느덧 두 배로 불어난 불사(不死)의 군단이 살아 있는 것들을 덮쳤다.

콰아아앙!

- 그어어어어!

무수한 비명과 죽음으로 뒤덮여 가는 사막.

그 광경을 멍하니 바라보던 샤오 쉔은 잠시 잊고 있던 자신의 임무를 떠올렸다.

“본부. 본부 응답 바람.”

치익.

통신 마법이 부여된 무전기가 노이즈와 함께 마나가 뒤섞인 전파를 흘려보냈다.

대기에 스며든 불안정한 마력을 비집고, 멀리. 더 멀리.

그리고 샤오 쉔의 다급한 통신이 마침내 본대에 닿았을 때.

“Company-halt!”

활주로에 한 치의 흐트러짐 없이 도열한 군인과 헌터들 사이로, 누군가를 실은 항공기가 부드럽게 착륙했다.



* * *



이번 토벌전은 헌터만 무려 10만에 세계 각국이 연합한 초대형 작전. 아니, 전쟁이나 다름없다.

그런 만큼 본대에는 상당한 숫자의 헌터가 잔류 중이었고, 군인들은 발에 챌 만큼 득실거렸다.

다국적에, 다인종으로 이루어진 군대.

세계 헌터 연맹은 혹시 모를 지휘 계통 분산을 대비하여 본대를 책임지는 인물을 신중히 선별해야 했고, 훌륭한 조언자인 최 팀장은 내게 한 사람을 추천했다.

헌터로서 쌓아 올린 뛰어난 무력과 전공. 동시에 대규모 군대를 운영할 수 있을 만큼의 전략과 지식을 갖춘 자.

헌터와 군인.

두 직업군에서 짬밥의 끝판왕을 찍은 유일무이한 인물.

바로 대격변 때부터 활동해 온 S급 헌터이자, 천조국의 전(前) 국방장관이었던 척 헤이글이었다.

“오. 잠자는 숲속의 공주께서 드디어 오셨군. 아니면 겨울잠이라도 잔 건가?”

나를 향한 척 헤이글의 인사 아닌 인사에, 좌우로 도열해 있던 이들 사이에서 낮은 웃음소리가 흘러나온다.

물론 다음 순간 씻은 듯이 사라져 버렸지만.

“웃어? 이 엿 같은 전시 상황이 그렇게 장난 같나?”

“…….”

“이런 정신 나간 개자식들. 앞으로 내 앞에서 웃었다간 누구든 지위 고하를 막론하고 작살 내 주마. 희멀건 피부를 인생 최대 업적으로 생각하는 얼빠진 양키 새끼건, 정치적 올바름 같은 개소리나 지껄이는 검둥이건, 틈만 나면 스마트폰만 쳐 보고 있는 옐로우몽키건 가리지 않고 반 죽여 놓을 거야. 알아들었나?”

“Yes. sir!”

“빌어먹을. 목소리가 작다!”

“Yes!! sir!!”

모두가 목이 터져라 외치자, 그제야 고개를 끄덕인 척 헤이글이 시가를 한 모금 빨았다.

“Ok. ladies.”

“…….”

미친 패기 보소.

확실히 자타가 공인하는 살아 있는 전설이라 그런지, 무대를 뒤집어 놓는 실력이 김수단 선배님도 한 수 접어 줄 정도다.

물론 이런 빠릿빠릿한 분위기가 연출되기까지는 불곰마냥 두꺼운 저 팔뚝과 타고난 폭력성이 크게 한몫했겠지만.

‘확실히 책임자로는 적격이네.’

내심 중얼거린 그때, 활주로를 맹렬하게 가로지른 군용 지프 차 한 대가 우리 앞에 멈춰 서더니 정복을 걸친 군인 하나가 다급하게 외쳤다.

“몬스터 웨이브! 몬스터 웨이브로 인한 긴급 지원 요청입니다!”

아마 내가 평범한 여행객이었다면 시차 적응을 위해 하루 정도 휴식을 취했을 거다.

하지만 이미 내 삶은 평범이라는 단어와는 결별한 지 오래였고, 두 번 다시 재결합할 여지는 없었다.

“어딥니까, 그곳이.”
```

## Final English reading copy

```markdown
# Chapter 792

“…What is that?”

Xiao Shen turned at the words, but he couldn’t see anything strange. The Skeleton King, however, could.

Even though Magic Johnson’s illusion magic had given him a human appearance, he was fundamentally a monster.

And not just any monster—one of the highest-ranking undead.

The sensation gripping the Skeleton King at that moment was something connected to the very source of his power.

*Damn it. This is…*

There was no doubt.

The feeling was faint, but unmistakable.

Beneath a dark sky that swallowed even the moonlight, he sensed the energy of death scattering across the endless desert.

There wasn’t a single drop of blood or a corpse in sight, but the Skeleton King recognized the energy stirring his instincts from beyond the darkness: death qi.

He knew, too, what had happened to the search squad that had suddenly gone silent about an hour ago.

“Young human brat.”

“Yes?”

“Contact the main force at once. Tell them we found the search party.”

“……!”

The desert was still, without a trace of anyone. But the Skeleton King’s words were the opposite of reassuring.

Xiao Shen finally understood what was happening. His face stiffened as he nodded, and the Skeleton King started walking, following his instincts.

*Crunch. Crunch.*

Footprints pressed into the desert as grains of sand crumbled beneath them.

After about ten steps, the Skeleton King suddenly stopped and muttered under his breath.

“Whoever did this buried them deep.”

And the next moment—

*Fwoosh!*

A section of the desert, stretching out like an endless sea, surged into the air.

A vast wave of magical power poured from a single gesture, holding the sand aloft. When the twenty bodies buried beneath it came into view, the Skeleton King froze before he could stop himself.

“……!”

A recent memory—one from not so long ago—flashed through his mind like lightning.

At the same time, an ominous premonition swept over him.

*Wait. Then could it be…*

But the Skeleton King’s thoughts didn’t get far. No—they couldn’t.

*Whoosh.*

A chill wind blew from somewhere, sweeping sand through the air.

And something was mixed in with it.

The Skeleton King stared toward some distant part of the desert, swallowed in pitch-black darkness. Then he asked Xiao Shen, who still hadn’t noticed anything.

“Have you contacted the main force?”

“Yes. They replied that they’re sending the nearby support team right away…”

“How long will it take?”

“They estimate thirty minutes at most.”

“Thirty minutes. That’s a little close.”

The Skeleton King clicked his tongue.

“I’m not sure I can protect anyone.”

“……?”

“Hmm.”

He looked Xiao Shen up and down. Then, with a sigh, he said, “Listen, young human brat. I’m giving you two missions.”

“Ah, yes! I’ll do anything you ask, Teacher King.”

“Good attitude. First, take out that damned special radio of yours and contact the main force again.”

“What should I tell them?”

“Tell them to send the best people they can, as fast as they can. Not that weak support team riding in on turtles. Got it?”

Xiao Shen had no idea why collecting the bodies would require that much urgency and manpower, but he nodded without hesitation.

The person he respected most in the world was Jin Taekyung, and the Skeleton King was Jin Taekyung’s friend.

“Understood. What’s the second mission?”

But the answer that followed was so unexpected that even Xiao Shen had to ask again.

“Pick up a weapon.”

“What?”

“And protect yourself. If you don’t think you can, you can run.”

“W-wait a second.”

What was he talking about?

Xiao Shen blinked, trying to make sense of the baffling order. It didn’t take long before he understood what the Skeleton King meant.

*Rrrumble. Rrrumble.*

An unknown tremor traveled through the ground.

As the vibration grew stronger, countless grains of sand bounced up around them. Then the Skeleton King spoke, turning Xiao Shen’s dawning suspicion into certainty.

“A lot of them.”

“……!”

Xiao Shen didn’t answer.

His mouth hung open as he stared at the far-off desert horizon. In his eyes, darkness writhed like a living thing.

No—in numbers too vast to count.

*Monster Wave…!*

At the moment the words that had become humanity’s nightmare struck Xiao Shen’s mind—

*Crunch.*

The Skeleton King walked toward the rapidly approaching tide of monsters.

There was no fear or hesitation in his steps. The mighty magical power surging from him reached ever outward.

> “By the name of the King, I command you.”

His low voice echoed across the desert. It pierced the thick darkness and roused the spirits crushed beneath the weight of ages and countless grains of sand.

> “Answer the call.”

*Rrrumble!*

A quake-like tremor swept through the desert.

At their king’s call, steeped in the energy of death, spirits that had lain in deep slumber burst through the sand and rose to the surface.

*Crackle!*

Pale sand scattered through the air. In the darkness, white bones gleamed.

*Grrr.*

An Arabian leopard, its beautiful hide lost in death, stretched its limbs. Wolves and hyenas shone with green eyes as dozens of eagles soared powerfully above them, spreading wings stripped down to bone.

*Eeeee!*

Their sharp cries split the night sky. The eagles, their wings spanning several meters, glided high overhead.

They passed above the monster army charging across the ground in a storm of sand, then scattered toward the vast desert and woods. They had only one mission:

Find a certain being who wasn’t here, by the King’s command.

> “Somewhere in this desert, there’s something that carries the scent of humans. Find it. No matter what.”

The eagles beat their wings with all their strength.

They had magical power to carry them on the wind instead of feathers, and though they’d lost the life within them, their vitality would never run dry.

*Whoosh!*

From far below, the King watched the flock of eagles disappear into the distance. Remembering the human bodies he’d uncovered moments ago, he walked toward the monster army bearing down on him.

*What kind of trace was it?*

*Whoosh—BOOM!*

A massive wave of magical power burst from the Skeleton King’s outstretched fist and swallowed the monsters at the front.

At the same time, a hundred or so beasts rushed into the empty space and tore into the enemy.

*Yowww!*

*Smack!*

An orc’s upper body went flying under the swipe of a leopard’s forepaw. A pack of hyenas nimbly dodged a club crashing down from above, then sank their teeth into a troll’s body.

*Crunch!*

The numbers were hopelessly against them.

But the moment the battle began, the Skeleton King understood: absorbing some of Michael Silbert’s magical power had strengthened his own powers enough to give even these spirits—once mere wild beasts—the strength to crush ordinary monsters in an instant.

*Splatter! Rrrumble!*

*Graaaah!*

Blood and flesh flew as the living screamed.

The enemy formation began to crumble in moments.

The Skeleton King knocked the heads off three ogres with a single strike, then looked toward some dark corner of the desert.

He couldn’t see a thing, but he knew.

Whatever had killed the search party had already left this place and disappeared somewhere out in the desert.

*What the hell are you?*

The question he asked himself went unanswered. The Skeleton King stared into the darkness with sunken eyes, then raised an ogre lying like a rotten log from the dead.

No—not just the ogre. Everything around him.

> “Answer the call.”

*Fwoosh.*

A dazzling golden radiance spread in every direction, brilliant enough to be mistaken for something other than magical power.

The immortal army, now twice its former size, descended upon the living.

*BOOM!*

*Grrrrr!*

The desert was gradually buried beneath countless screams and death.

As Xiao Shen stared blankly at the sight, he remembered the task he’d temporarily forgotten.

“Base. Base, please respond.”

*Chhh.*

The radio, enchanted with communication magic, transmitted a mana-laced signal amid a burst of static.

It pushed through the unstable magical power permeating the air, farther and farther.

And when Xiao Shen’s urgent message finally reached the main force—

“Company, halt!”

An aircraft carrying someone landed smoothly among the soldiers and Hunters standing in perfect formation along the runway.

* * *

This expedition involved a hundred thousand Hunters and a coalition of nations from across the world. It was a massive operation—or, more accurately, a war.

As a result, a considerable number of Hunters remained at the main base, and soldiers were everywhere you looked.

An army made up of different nations and races.

The World Hunter Federation had to carefully choose someone to lead the main force, in case command fractured at a critical moment. Team Leader Choi, an excellent adviser, recommended a man for the job.

Someone who’d built up extraordinary strength and a distinguished record as a Hunter, while also possessing the strategy and knowledge needed to command a large army.

A Hunter. A soldier.

The one and only man to have reached the top of the ladder in both professions.

Chuck Hagel—an S-rank Hunter active since the Great Cataclysm and the former Secretary of Defense of the good ol’ U.S. of A.

“Oh. Sleeping Beauty finally decided to show up. Or did you take a long winter’s nap?”

Chuck Hagel’s not-quite-a-greeting drew quiet laughter from the people lined up on either side of me.

It vanished without a trace the next moment.

“You’re laughing? Does this fucked-up wartime situation look like a joke to you?”

“……”

“You lunatics. From now on, anyone who laughs in front of me is getting their ass kicked, rank be damned. I don’t care if you’re some pasty Yankee dumbass who thinks white skin is your greatest achievement in life, a darkie spouting bullshit about political correctness, or a yellow monkey who can’t stop staring at his smartphone. I’ll beat every last one of you half to death. Understood?”

“Yes, sir!”

“Goddamn it. I can’t hear you!”

“Yes, sir!”

Only after everyone shouted at the top of their lungs did Chuck Hagel nod and take a drag from his cigar.

“Okay, ladies.”

“……”

That was one hell of a force of personality.

He really was a living legend by anyone’s standards. Even Senior Kim Soodan would have to admit Hagel had him beat at bringing down the house.

Of course, those thick arms like a bear’s and the violence he was born with had a lot to do with creating this brisk atmosphere.

*He really is the right man to be in charge.*

Just as I thought that, a military jeep came tearing across the runway and screeched to a stop in front of us. A soldier in dress uniform hurriedly called out.

“Monster Wave! We’ve received an urgent request for support because of a Monster Wave!”

If I’d been an ordinary traveler, I would’ve taken a day to recover from jet lag.

But my life had parted ways with the word *ordinary* a long time ago, and there was no chance of them ever getting back together.

“Where?”
```
