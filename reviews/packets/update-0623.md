<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0623.txt",
      "sha256": "cad53d97258adfcfa7ecceffb895c12b38b3ccfa1c6a9356b60057c9fec4f068",
      "bytes": 12834
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ad0066e93b259aba46ef8fb114f40bc13af8c7b6a5022d7a9d48b416da82382",
      "bytes": 2150
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e0fbcccc37c6980166cb9039edeae9ae662d8b3192d9f14b32695b7785bbbc8c",
      "bytes": 192996
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f5087901de90b61df9c560181a65b92de6b7780dfc06d896e195d82fcfa62ac",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "68c4bb02cd7bced3fc7e86c1e839bf3e01777d73323412cbea261c74f1f63a60",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "6eeba7c2e5851fb1866b02b6eef455021a5c6a11fa7917c5d8c22764a7da17a5",
      "bytes": 988
    },
    {
      "path": "characters/Namho.md",
      "sha256": "1e8014b30c6de07bf1ace9327bcf44995f6fcb3c8b20ed253a55f3aefd88414f",
      "bytes": 843
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "535111962df58fd6f7e270746966d4cabf500aec09961ad7bf447c7b2d834435",
      "bytes": 196394
    }
  ],
  "estimated_tokens": 9957
}
-->

# Durable State Update — Chapter 623

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 623. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 623. Profile updates may replace only one
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
  "chapter": 623,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 623,
    "continuity_sources": [623],
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
    "The Fire Dragon Pavilion has reached the directly administered outer territory of the Nanman Beast Palace, a vast pastureland that serves as the palace's capital-like domain.",
    "The Nanman Beast Palace Quest is Grade Supreme Peak and requires Jin Taekyung and the Fire Dragon Pavilion to arrive at the palace.",
    "The Quest's reward is an unknown Chain Quest.",
    "The Nanman Beast Palace governs a kingdom-like territory spanning five counties, and outsiders are forbidden to enter beyond its fences.",
    "The party is concealing its identities because Nanman's non-Han peoples are hostile toward Han Chinese.",
    "Dark Heaven is targeting Nanman, and Taekyung believes a catastrophe involving the rift is imminent.",
    "The Beast Miao King participated in the Great Faction War and is believed to favor Jeok Cheongang and the Fire Gate Clan.",
    "Livestock and other living things within the Nanman Beast Palace's territory are valuable protected property.",
    "Namho is an eighty-year-old Miao elder who has spent more than fifty years in Nanman and is guiding the Fire Dragon Pavilion.",
    "Namho's emergency signal firework ignited the pasture, and a wild-beast-like figure emerged beyond the flames."
  ],
  "continuity_sources": [
    622
  ],
  "open_questions": [
    "Was the woman in the Heavenly Demon Escort Bureau group the Southern Heaven Demon Empress?",
    "Who poisoned and killed the Heavenly Demon Escort Bureau group, and why?",
    "What catastrophe will Dark Heaven cause in Nanman?",
    "What dangers and response await the Fire Dragon Pavilion inside the Nanman Beast Palace?",
    "Who or what appeared beyond the burning pasture, and what consequences will the fire cause?"
  ],
  "safe_through": 622,
  "temporary_decisions": [
    "Render 南琥, Namho's code name, as Namho rather than translating it literally as southern amber.",
    "Use Elder Chao for the local title 챠오 어르신.",
    "Render 애뇌산 as Ailao Mountain.",
    "Render 혈생균 as blood-feeding fungus.",
    "Render 直轄地 as directly administered territory."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 주화란    | **Ju Hwaran**      |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장법     | **palm technique**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 621
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 621
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 622
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 622
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

## Korean source

```text
＃623화



보기 좋게 그을린 갈색 피부와, 날렵한 체형임에도 전신 곳곳에 보기 좋게 자리 잡은 잔근육.

한눈에 보기에도 중원의 한족과 구별되는 이색적인 생김새를 지닌 이민족 청년은 언덕 아래의 광경을 바라보며 생각했다.

‘……이게 무슨 일이지?’

그런 의문이 드는 것은 당연했다. 그의 눈앞에서 드넓은 목초지가 활활 불타고 있었으니까.

지금 이 순간에도 빠르게 번져 나가는 화염은 쉴새 없이 검은 연기를 토해 냈고, 그 사이로 소와 양, 말 따위의 가축들이 정신없이 도망치는 중이었다.

- 크르릉.

그때 문득 아래로부터 전해진 낮은 울음소리와 떨림. 청년은 눈처럼 새하얀 백호(白虎)의 갈기를 부드럽게 쓰다듬었다.

“괜찮다. 괜찮아.”

- 크륵.

“녀석, 단단히 화가 났구나.”

마음은 언어로만 전해지는 것이 아니다.

비록 인간과 짐승으로 종족은 다르나, 오랜 세월을 함께 한 그들은 작은 몸짓 하나, 울음소리의 높낮이만으로도 서로의 뜻을 알 수 있었다.

백호의 푸른 눈동자와 시선이 닿은 이민족 청년이 고개를 끄덕였다.

“그래. 우선 불길부터 잡자. 침입자들을 처벌하는 것은 그다음이다.”

이대로 놔뒀다가는 걷잡을 수 없이 커진 불길이 목초지 전체를 잿더미로 만들 판국이다.

물론 땅이야 다시 복구되겠지만, 그동안 불길에 휩싸여 죽어 갈 가축들을 구해야 했다.

그리고 다음 차례는…….

‘감히 이런 짓을 벌이다니.’

남만야수궁의 영역을 허락받지 않고 침범한 것으로도 모자라, 불까지 지른 괘씸한 놈들을 치죄(治罪)해야 한다.

저 멀리, 매캐한 연기 너머로 흐릿하게 보이는 정체불명의 침입자들을 노려본 이민족 청년은 백호의 갈기를 쓸어내렸다.

그의 뜻을 알아차린 하얀 맹수가 바람처럼 쏘아졌다.

- 크아아앙!

천둥 같은 포효가 불길을 뚫고 울려 퍼졌다.



* * *



말 그대로 순식간이었다.

언덕 위에서 갑작스럽게 나타난 한 마리의 백호와 이민족 청년이 한 몸이라도 된 것처럼 사방으로 동분서주하기 시작한 것은.

화륵, 콰아아아!

‘저거 어릴 때 학습만화에서 본 것 같은데.’

이른바 맞불이라고 하나?

불과 불이 부딪친다. 다른 하나가 사라질 때까지 서로를 집어삼킨다. 청년이 능숙한 솜씨로 피워올린 맞불의 효과는 대단했다.

언제 그랬냐는 듯이 빠르게 사그라지는 불길의 모습에, 나도 양심상 한 몫 거들기 위해 앞으로 나섰다.

퍼엉!

짧게 끊어치듯 내지른 일권(一拳)에 불길이 바람 앞의 촛불처럼 휘청 거리……다가 더욱 커졌다.

콰아아아!

“오메.”

뭐야, 이거.

당황해하는 내게 남호가 비명처럼 외쳤다.

“이런 미친! 도대체 무슨 짓을 한 건가!”

“……지금 그게 남 노인이 할 말입니까? 무슨 방귀 뀐 놈이 성내는 것도 아니고. 불 지른 사람이 뭐라고 하네.”

“나도 그렇게 될 줄 몰랐지!”

“저도 마찬가집니다.”

“지금 그게 문젠가! 어서 불길부터…… 어어, 어어어! 뒤! 뒤!”

콰아아아아!

“거 엄살은. 아직 괜찮습니다.”

불길이 엄청 강해진 건 아니지만 한시라도 빠르게 수습해야 하는 건 맞다.

마음이 다급해진 나는 더 생각해 볼 것도 없이 몸집을 부풀린 불길을 향해 연달아 손바닥을 내질렀다.

그리고 다음 순간 깨달았다.

‘어, 맞다.’

내가 방금 사용한 장법의 이름이 화염신장(火焰神掌)이라는 것을.

쿠화아아아아아!

조금 전까지는 아니었지만, 이제는 자신 있게 말할 수 있다. 불길이 엄청나게 강해졌다.

그건 한편으로는 기적 같은 광경이었다. 거의 빈사 상태에 빠져 있던 불길이 처음보다 몇 배는 거대하게 타오르기 시작했으니까.

물론 사방으로 미친 듯이 도망치는 가축들에게는 지옥 같은 광경이었겠지만.

“……어.”

거의 불지옥이 되어 버린 주변과 내 손바닥을 말없이 번갈아 보던 나는 이글거리는 화염 너머로 이곳을 노려보고 있는 두 쌍의 눈동자와 시선이 딱 마주쳤다.

언덕에서 나타났던 백호와 바로 그 이민족 청년이다. 눈의 색깔도, 종족도 달랐지만 둘의 공통점이 있다면 개빡쳐 있다는 거다.

“노옴! 이게 도대체 무슨 짓이냐!”

- 크아아앙!

나이도 어려 보이는 놈이 초면에 반말이라니.

분명히 선을 넘은 행동이지만 그 선을 태워 버린 건 나다. 나는 21세기 문명인답게 정중하면서도 침착한 태도로 그들을 안심시켰다.

“누군지는 모르겠지만 우선 걱정하지 마. 내가 해결할게.”

물론 내가 안심시킨다고 해서 상대방이 안심할 거라는 보장은 없다. 바로 이번처럼.

“아니다! 안 돼!”

- 크아아아앙!

나는 일심동체처럼 외치는 일인일호(一人一虎)를 점잖게 타일렀다.

“괜찮아. 할 수 있어. 그보다 호랑이 좀 조용히 시켜 줄래?”

“안 된다. 이노옴!”

- 크아아아아앙!

“하지 마?”

“하지 마!”

- 크아아아아아앙!

음. 불길만큼이나 거센 반발이군. 하지만 나는 고개를 가로저었다.

“아냐. 할래. 나는 날 믿어.”

“이 미친 한족 색……!”

- 크아앙……!

백호와 이민족 청년의 부르짖음이 끝나기도 전, 나는 섬전 같은 속도로 쌍장(雙掌)을 떨쳤다.

후우우웅, 퍼버벙!

허공을 격하고 쏘아진 두 줄기의 강맹한 장력(掌力)이 넘실거리는 불의 파도를 가르고 터트린다.

그러나 여기에서 멈춘다면 불길은 더욱 거세질 것이고, 그건 지금까지의 실수를 반복하는 짓밖에 안 된다.

나는 망설임 없이 연이어 장력을 쏘아 보냈다.

퍼벙! 퍼어엉!

사람들이 불길을 쉽게 잡지 못하는 이유는 간단하다.

불을 끌 만한 물이 부족해서, 혹은 불길을 촛불처럼 꺼트릴 만큼 강한 바람이 없어서.

그러니 결국 더욱 많은 물이나 강한 바람이 있으면 되는 것이고, 지금의 경우는 후자였다.

퍼어엉!

마지막으로 쏘아 보낸 장력은 특히나 강맹했다.

흡사 태풍과도 같은 바람이 목초지를 휩쓸자, 정신없이 도망치던 가축들의 몸이 일순 붕 떠오르고 모든 풀과 나무과 납작 엎드렸다.

그리고…….

솨아아악.

사방으로 번져가던 화염이 순식간에 사그라졌다.

이제 남은 것은 모닥불처럼 작게 타들어 가는 불씨와 검은 재로 화한 일부 목초지.

그리고 그 광경을 멍하니 바라보는 어느 이민족 청년과 새하얀 호랑이 한 마리뿐이었다.

“이, 이게 무슨…….”

- 크르릉?

믿을 수 없다는 듯한 두 쌍의 시선.

가까운 곳에 남아 있는 마지막 불씨를 발로 비벼끈 내가 어깨를 으쓱해 보였다.

“말했잖아. 할 수 있다니까.”

“……!”

- ……!

순수한 놀라움이 떠오른 눈동자로 나를 응시하던 이민족 청년이 손에 든 창을 겨누며 물었다.

“나는 남만야수궁의 야율목이다. 당신은?”

당연한 소리겠지만 역시 남만야수궁의 인물이었군.

고개를 끄덕인 내가 막 대답하려던 그 순간이었다.

“그는 태원진가의 진태경이라고 하네.”

등 뒤에서 불쑥 울려 퍼진 늙수그레한 목소리. 고개를 돌린 내 시선에 어느새 가까이 다가온 화룡각 대원들과 선두에 선 남호가 들어왔다.

“중원에서는 열화신룡(熱火神龍)이라 불리는 당대 제일의 후기지수이며, 무림맹에 속한 화룡각의 각주이기도 하지.”

내 이름과 별호가 남만까지 알려져 있는지는 모르겠다.

그러나 최소한 눈앞의 이민족 청년, 아니 야율목은 남호가 뒤에 덧붙인 말을 정확히 알아들은 것 같았다.

“무림맹…….”

낮은 목소리로 뇌까린 야율목이 백호의 갈기를 쓰다듬는다.

으르렁거리던 맹수의 울음소리가 차츰 가라앉는 것을 가만히 지켜보던 그가 나를 겨누고 있던던 창을 내리며 신형을 돌렸다.

“따라오시오. 무림맹라는 말이 나왔으니 지금 당장은 참겠지만, 두 번 다시 아까와 같은 헛짓거리는 하지 말고.”

남호가 어깨를 으쓱해 보였다.

“실수였네. 하지만 명심하지.”

“그래야 할 거요. 비명횡사하고 싶지 않다면.”

백호를 탄 채 앞서가는 야율목의 뒷모습을 바라보던 내가 떨떠름한 표정으로 남호에게 말했다.

“어린놈이 싸가지가 없네요. 불 지른 건 잘못이긴 하지만.”

“거기 한족, 다 들린다.”

- 크르릉.

“들으라고 한 거야. 인마.”

“뭐?”

“어르신한테 말본새하고는. 넌 할아버지도 없냐?”

순간 울컥한 표정을 지었지만 그뿐이다.

나를 한 차례 노려본 야율목이 다시 돌아서자, 내 뒤를 따라 걸음을 옮기던 남호가 짜게 식은 눈빛으로 입을 열었다.

“말조심하게.”

“남 노인 편 들어 준 겁니다. 안 그래도 오늘내일하시는 분한테 비명횡사라는 말이 가당키나 합니까?”

“내가 언제 오늘내일…… 됐네. 애초에 기대를 말아야지. 혹시 평지풍파를 하루라도 못 일으키면 즉사하는 병이라도 앓고 있나?”

“혹시 남만야수궁 소유의 목초지에 불 안 지르면 노망나는 병이라도 앓고 있습니까?”

“…….”

“지팡이 석 달 압수하기 전에 스스로를 돌아보십쇼.”

딜 교환에서 씹손해를 본 남호가 한숨을 내쉬었다.

“좋아, 인정하지. 명백한 내 실수였네. 오십여 년이나 묵혀 둔 물건이라 다루는 데 조심했어야 했어.”

“시원시원하게 인정하는 모습, 보기 좋습니다. 목초지는 아직도 후끈후끈하지만요.”

“……자네 말을 들을 때마다 뼈마디가 욱신거리는군. 하지만 저 청년을 대할 때는 조금이라도 주의하게.”

“왜요?”

“왜긴, 스스로 말하지 않았나. 야율목이라고.”

“야율목인지 야율모기인지. 뭐 어쩌라고…….”

대답하던 나는 문득 말꼬리를 흐렸다. 기억 속에서 잊고 있던 무언가 생각날 듯 말 듯 해서다.

‘야율목. 야율목이라.’

곰곰이 생각하던 나는 고개를 돌려 주화란에게 물었다.

“저기, 주 소저.”

“네?”

“혹시 남만야수궁주 이름이 뭐였죠?”

“야수묘왕(野獸苗王)을 말씀하시는 건가요?”

“예.”

남만야수궁의 궁주인 야수묘왕은 남만에서 가장 강성한 부족 중 하나인 묘족(苗族)의 우두머리이자, 이민족이라는 출신 성분과는 별개로 십왕(十王)의 말석을 차지한 인물이다.

나를 향해 빙긋 웃은 주화란이 친절한 어조로 대답했다.

“야율척이요.”

“아하. 그렇군요.”

“네. 야율이 성씨예요. 남만에서도 쉽게 찾아볼 수 없는 희귀한 성이죠.”

“그럼 저 싸가지 없는 친구는 야 씨겠네요. 이름이 율목이고.”

“죄송한데, 혹시 그게 사실이길 바라시는 건가요?”

“음. 그렇다면요?”

주화란이 막 입을 떼려던 그 순간, 한참 앞에서 백호를 타고 이동하던 야율목의 앞을 가로막고 있던 숲이 흔들렸다.

파스슥. 타닥!

장담컨대, 이렇게 다양한 동물을 한 자리에서 보는 건 일곱 살 때 갔던 동물원 이후로 처음이다.

전신이 흑색 털로 뒤덮인 재규어와 호랑이, 거기다 표범과 코끼리까지.

갖가지 맹수에 올라타 있던 이민족 사내와 여인들이 야율목을 발견하고 황급히 안장에서 내려 엎드려 부복했다.

“소궁주!”

“무사하십니까!”

“불길이 일어났다는 급보를 받았습니다. 소궁주께서 이리 앞뒤 가리지 않으시면 궁주께서 심려가 크시…… 그런데 저자들은 누구입니까?”

맹수와 사람이 뒤섞인 수십 쌍의 시선.

그들이 앞서 외쳤던 소궁주라는 단어와 그보다도 이전에 할아버지도 없냐 물었던 내 말을 조용히 곱씹어보던 나는 슬그머니 야율목의 옆으로 다가가 어깨동무를 하며 말했다.

“친굽니다. 그렇지, 목아?”

“…….”

야, 웃어.
```

## Final English reading copy

```markdown
# Chapter 623

With his handsome brown skin darkened by the sun and fine muscles settled attractively across his lean frame, the non-Han young man possessed an unusual appearance that marked him as different from the Han Chinese of the Central Plains.

As he gazed at the scene below the hill, he thought,

*…What is going on?*

His confusion was only natural. A vast pasture was blazing before his eyes.

Even now, the rapidly spreading flames were belching endless clouds of black smoke, while cows, sheep, horses, and other livestock fled frantically through the chaos.

*Grrrr.*

A low growl and tremor suddenly reached him from below. The young man gently stroked the snow-white mane of the white tiger beneath him.

“It’s all right. It’s okay.”

*Grrk.*

“You’re really angry, aren’t you?”

Feelings were not conveyed through words alone.

Though human and beast belonged to different species, they had spent so many years together that they could understand each other through the slightest gesture or the rise and fall of a growl.

The non-Han young man met the white tiger’s blue gaze and nodded.

“That’s right. We’ll put out the fire first. Punishing the intruders comes afterward.”

If they left it alone, the flames would grow beyond control and turn the entire pasture into ashes.

The land could be restored, of course, but they still had to save the livestock that would otherwise be swallowed by the flames and die.

And then came the next matter…

*How dare they do something like this?*

As if trespassing into the Nanman Beast Palace’s territory without permission were not enough, those insolent bastards had even set it on fire. They had to be punished.

The non-Han young man glared at the mysterious intruders barely visible through the distant, acrid smoke and stroked the white tiger’s mane.

The white beast understood his intention and shot forward like the wind.

*Kraaaar!*

A thunderous roar rang out through the flames.

* * *

It happened in the blink of an eye.

A white tiger and a non-Han young man had suddenly appeared on the hill, then began rushing about in every direction as though they had become one body.

*Whoosh—roar!*

*I think I saw something like this in an educational comic when I was little.*

Was this what they called fighting fire with fire?

One fire collided with another. They devoured each other until one disappeared. The young man’s skillfully raised backfire was remarkably effective.

As the flames quickly died down as if nothing had happened, I stepped forward to lend a hand out of sheer conscience.

*Boom!*

I struck out with a short, sharply cut-off punch. The flames wavered like a candle in the wind…

…and then grew even larger.

*ROOOOAR!*

“Good grief.”

What the hell was this?

As I stood there in confusion, Namho shouted at me like he was screaming in agony.

“This is insane! What the hell did you do?”

“…Is that really something for Old Man Nam to say? It’s like the one who farted getting angry. The person who set the fire is complaining.”

“I didn’t know it would turn out like this!”

“Neither did I.”

“Is that what matters right now? Put out the fire first… Oh, oh, oh! Behind you! Behind you!”

*ROOOOAR!*

“Don’t be so dramatic. It’s still fine.”

The flames had not become overwhelmingly powerful, but we did need to deal with them as quickly as possible.

Pressed for time, I sent a series of palm strikes toward the flames that had suddenly swollen in size without giving it any further thought.

And then I realized.

*Oh, right.*

The name of the palm technique I had just used was the Flame Divine Palm.

*Fwoooooosh!*

The flames had not been this strong a moment ago, but now I could say it with confidence.

They had become enormously powerful.

In one sense, it was almost a miraculous sight. Flames that had been nearly extinguished were now roaring several times higher than before.

Of course, to the livestock fleeing madly in every direction, it was probably a scene straight out of hell.

“…Huh.”

I silently shifted my gaze between the near-inferno around us and my palms. Beyond the raging flames, I met the eyes of two pairs of furious eyes glaring at me.

They belonged to the white tiger that had appeared on the hill and the non-Han young man.

Their eye colors and species were different, but they had one thing in common.

They were both absolutely pissed off.

“You bastard! What do you think you’re doing?”

*Kraaaar!*

The kid looked young, yet he was speaking casually to me on our first meeting.

Clearly, he had crossed a line—but I was the one who had burned that line down. As a civilized man of the twenty-first century, I reassured them with a polite and composed attitude.

“I don’t know who you are, but don’t worry. I’ll handle this.”

Of course, there was no guarantee that the other party would feel reassured just because I had reassured them.

As demonstrated by the immediate response.

“No! You can’t!”

*Kraaaar!*

I gently admonished the one man and one tiger shouting in perfect unison.

“It’s okay. I can do this. More importantly, could you quiet the tiger down a little?”

“No! You cur!”

*Kraaaar!*

“Don’t?”

“Don’t!”

*KRAAAAR!*

Hmm. They were putting up as much resistance as the flames.

But I shook my head.

“No. I’m going to do it. I trust myself.”

“You crazy Han Chinese bas—!”

*Kraaaar…!*

Before the white tiger and the young man could finish shouting, I struck with both palms at lightning speed.

*Whoooosh—boom!*

Two streams of mighty palm force shot through the air, splitting apart and bursting through the rolling waves of fire.

But if I stopped there, the flames would only grow more intense. That would simply mean repeating the mistakes I had already made.

Without hesitation, I fired off one palm force after another.

*Boom! Boom!*

The reason people had difficulty putting out fires was simple.

Either they lacked enough water to extinguish the flames, or they lacked wind strong enough to snuff them out like a candle.

In the end, all they needed was more water or stronger wind.

And in this case, the latter would do.

*Boom!*

The final palm force I sent out was especially powerful.

A wind like a typhoon swept across the pasture. The livestock that had been fleeing in panic were briefly lifted from the ground, while every blade of grass and every tree was flattened.

And then…

*Whoosh.*

The flames spreading in every direction died down in an instant.

All that remained were small embers burning like a campfire and patches of pasture reduced to black ash.

And standing there, dumbfounded by the sight, were a non-Han young man and a single snow-white tiger.

“What… What is this?”

*Grrrr?*

Two pairs of eyes stared at me as if they could not believe what they were seeing.

I walked over to the last ember nearby, ground it out beneath my foot, and shrugged.

“I told you. I can do it.”

“……!”

*……!*

The non-Han young man stared at me with eyes filled with pure astonishment. Then he pointed the spear in his hand at me and asked,

“I am Yayul Mok of the Nanman Beast Palace. And you?”

As expected, he was a member of the Nanman Beast Palace.

I nodded and was just about to answer when an elderly voice suddenly rang out from behind me.

“He is Jin Taekyung of the Jin Family of Taiyuan.”

I turned around. The members of the Fire Dragon Pavilion had approached without me noticing, with Namho at the front.

“In the Central Plains, he is known as the Blazing Flame Divine Dragon, the foremost young prodigy of his generation. He is also the Pavilion Master of the Fire Dragon Pavilion, which belongs to the Murim Alliance.”

I did not know whether my name and sobriquet had reached Nanman.

But at the very least, the non-Han young man in front of me—Yayul Mok—seemed to understand the words Namho had added perfectly.

“The Murim Alliance…”

Yayul Mok murmured in a low voice and stroked the white tiger’s mane.

He quietly watched as the growling beast gradually calmed down. Then he lowered the spear pointed at me and turned around.

“Follow me. Since the Murim Alliance has been mentioned, I will let this go for now. But don’t do anything as foolish as that again.”

Namho shrugged.

“It was an accident. But I’ll keep it in mind.”

“You had better. Unless you want to die a sudden death.”

I watched Yayul Mok’s back as he rode ahead on the white tiger, then said to Namho with a sour expression,

“That kid is rude. Setting the fire was wrong, but still.”

“Hey, Han Chinese. I can hear you.”

*Grrrr.*

“I said it so you could hear me, punk.”

“What?”

“What kind of way is that to speak to an elder? Don’t you have a grandfather?”

Anger flashed across Yayul Mok’s face for a moment, but that was all.

After glaring at me once, Yayul Mok turned away again. Walking behind me, Namho gave me a flat, unimpressed look and said,

“Watch your tongue.”

“I was taking your side, Old Man Nam. Does it make any sense to tell someone who could drop dead any day that he’ll ‘die a sudden death’?”

“Since when could I drop dead any day…? Forget it. I should never have expected anything from you. Do you have some illness that’ll kill you on the spot if you go even one day without stirring up trouble?”

“Do you have some illness that makes you senile if you don’t set fire to a pasture owned by the Nanman Beast Palace?”

“……”

“Take a good look at yourself before I confiscate your walking stick for three months.”

Namho had taken a devastating loss in the exchange of insults, and he let out a sigh.

“All right. I admit it. This was clearly my mistake. It was something I had kept for more than fifty years, so I should have been more careful handling it.”

“It’s nice to see you admit it so cleanly. The pasture is still burning hot, though.”

“Every time I hear you speak, my bones start aching. But be a little careful when dealing with that young man.”

“Why?”

“Why else? Didn’t he say it himself? His name is Yayul Mok.”

“Whether he’s Yayul Mok or Yayul Mosquito, what do you want me to do about it…?”

I trailed off as I spoke.

Something forgotten in my memories felt as if it were about to come back to me.

*Yayul Mok. Yayul Mok…*

After thinking it over carefully, I turned to Ju Hwaran and asked,

“Excuse me, Young Lady Ju.”

“Yes?”

“What was the name of the Lord of the Nanman Beast Palace again?”

“Are you asking about the Beast Miao King?”

“Yes.”

The Beast Miao King, lord of the Nanman Beast Palace, was the leader of the Miao people, one of the most powerful tribes in Nanman. Regardless of his non-Han origins, he was also one of the Ten Kings, occupying the lowest position among them.

Ju Hwaran gave me a slight smile and answered in a kind voice.

“Yayul Cheok.”

“Ah. I see.”

“Yes. Yayul is his family name. It’s a rare surname that you don’t often encounter even in Nanman.”

“Then that rude little friend must be a Ya, I suppose. His name is Yulmok.”

“I’m sorry, but are you hoping that’s true?”

“Hmm. What if I am?”

Ju Hwaran had just opened her mouth to answer when the forest blocking Yayul Mok’s path far ahead of us began to shake.

*Rustle. Crackle!*

I could swear that this was the first time I had seen so many different animals gathered in one place since visiting the zoo at the age of seven.

Jaguars and tigers covered in black fur, along with leopards and even elephants.

The non-Han men and women riding various beasts spotted Yayul Mok. They hurriedly dismounted and prostrated themselves before him.

“Young Palace Lord!”

“Are you unharmed?”

“We received an urgent report that a fire had broken out. If Young Palace Lord continues acting so recklessly, the Palace Lord will be terribly worried… But who are these people?”

Dozens of pairs of eyes—human and beast alike—turned toward us.

I silently mulled over the title they had just called him, as well as my earlier question about whether he had a grandfather.

Then I slowly approached Yayul Mok, slipped an arm around his shoulders, and said,

“We’re friends. Right, Mok?”

“……”

“Hey, smile.”
```
