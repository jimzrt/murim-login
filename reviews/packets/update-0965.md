<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0965.txt",
      "sha256": "b943e045bf5bcd1c3ea678e125eb0049ed679db8f949fcb4f8b93d4e8139ffb8",
      "bytes": 13529
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a263be148d1e289a37242837588ff243538ab49e635b1b5dca9c91099266419e",
      "bytes": 1786
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a9abc25b921cbdce05f090e91781cabe86a577757b8e253bfe7473b3c6a55ce2",
      "bytes": 235304
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3c2e762153bfded1309e9e8f6d0afc6487d0b96b9a051c310770a5ec400bc1de",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "a9cbb9170b02a8be23821288bded07ebeb0ae36e68045e1239de42ce4e9d5768",
      "bytes": 1389
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "9c1af5d877eb6734c006cb5f57a82c982c2124c613a44d8ecab58819211b4fcf",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "37e19e0467234b45cbbaae5d189b109838afbd345811992a7e017233f86ec98d",
      "bytes": 269308
    }
  ],
  "estimated_tokens": 9453
}
-->

# Durable State Update — Chapter 965

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 965. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 965. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 965,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 965,
    "continuity_sources": [965],
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
    "Jin Wikyung has entrusted Lee Seowol with the battle’s aftermath and chosen to remain in the fight; his fate is unknown.",
    "Jin Mukyung refused Jamukha’s offer to spare him and the others in exchange for submission.",
    "An enemy attack has been signaled by horns; the force that caused the tremor is unidentified.",
    "Jin Mukyung killed the Demon Bird at Eight Spring Gorge and remains severely injured; Cheol Mubaek and Wipeng are gravely wounded.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    964,
    963
  ],
  "open_questions": [
    "Who is the approaching enemy force, and how will the battle and Mukyung’s confrontation with Jamukha unfold?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Jin Wikyung?"
  ],
  "safe_through": 964,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 팽철후    | **Peng Cheolhu**   |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 일신     | **One God**         |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 일격     | **One Strike**                         |
| 칭호               | **Title**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 황하 | **Yellow River** | River along which civilization began. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |
| 마조 | 진무경 | hostile opponents | you | familiar and blunt, with admiration | Calls him a young Sword Demon and speaks to him with growing respect. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 964
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 964
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 948
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong.

## Korean source

```text
＃965화



부우! 부우우우!

겹겹이 울려 퍼지는 뿔피리 소리는 앞서 울렸던 것과는 사뭇 달랐다.

하나의 거대한 울림으로 합쳐져야 할 그것은 뚝뚝 끊겨 있었고, 그 안에는 일말의 다급함마저 담겨 있었으니까.

그렇기에 뿔피리 소리에 담긴 정확한 의미를 알지 못하는 산서인들 또한, 눈앞의 적들에게 갑작스러운 이변(異變)이 발생했음을 직감할 수 있었다.

더불어 이 뜻밖의 변수가, 자신들에게는 생각지도 못한 행운이 되리라는 사실 역시도.

“지금! 지금이다!”

“물러서지 마라! 계속해서 몰아붙여라!”

지금 이 순간.

산서인들 중 무슨 일이 벌어졌는가에 대한 의문을 떠올리는 이는 없었다.

단 한 사람도.

그들 모두는 이미 죽음을 각오했다. 고향과 가족, 벗을 지키기 위해 이 자리에 남아 침략자들과 맞서고 있었다.

빼앗으려는 자와 지키려는 자.

마음에 품은 절실함의 크기도, 결의의 무게도 다르다.

산서인들은 젖 먹던 힘까지 쥐어 짜내어 비틀거리는 걸음을 내딛고, 어느 때보다 무겁게 느껴지는 병장기를 휘둘렀다.

뿔피리 소리에 담긴 의미를 깨닫고 주춤거리는 적들을 향해.

저 잔인무도한 초원의 침략자들을 향해.

카가가각!

푸푸푹!

예리한 날붙이들의 마찰로 불똥이 피어오른다.

당혹스러움으로 굳어 있던 케식들은 다급하게 맞섰으나, 찰나의 방심은 독기로 가득한 산서인들에게 기회로 돌아왔다.

서걱!

신월도를 타고 솟구친 도기(刀氣)에 서너 명의 팔다리가 날아간다. 하지만 아득한 고통 속에서도 숨이 끊기지 않은 그들은 온 힘을 다해 케식 십인장을 덮쳤다.

“이, 이 미친놈들이……!”

퍼걱!

섬뜩한 파육음과 뚝 끊겨 버린 외침.

정수리에 도끼가 찍히고도 살아남을 수 있는 사람은 그리 많지 않다.

아니, 없다.

“산서성을 넘본 대가다. 이 빌어먹을 오랑캐 새끼야.”

퉤.

눈을 부릅뜬 채 절명한 십인장의 시체에 가래를 뱉은 이름 모를 무림인은, 마지막 소명을 다하고 편안하게 눈을 감은 전우의 손아귀에서 조심스럽게 검 자루를 빼내었다.

먹먹한 목소리로 인사를 건네며.

“여기서 잠시만 쉬고 있게. 내 딱 열 놈만 더 죽이고 금방 돌아올 테니.”

사실 그도 안다.

아니, 산서인 모두가 안다.

영영 돌아오지 못할 수도 있다는 것을.

살아서는 두 번 다시 만나지 못하리라는 것을.

그러나 그 사실을 알고 있다 하더라도 달라지는 것은 없었다.

필사(必死)의 각오를 제외한다면, 아무것도.

으아아아아!

비명과도 같은 함성이 협곡을 떨어 울린다.

깊은 밤을 깨우고, 수십여 개의 뿔피리가 토해 내는 울림을 뚫고, 계속해서 멀리 저 멀리 나아갔다.

어둠에 잠긴 풀숲과 수많은 말발굽으로 다져진 지면을 스쳐, 어느 순간 높게 솟은 언덕 위에서 나타나 전장을 향해 내달리는 한 무리의 인마(人馬)에 닿을 때까지.

그리고 그들의 선두에 선 거구의 노인은, 산서인들이 토해 내는 그 치열한 함성을 들으며 미소지었다.

“그래. 똑똑히 듣고 있다. 노부가, 우리 모두가.”

두두두두두!

맹렬한 말발굽 소리가 지축을 두드린다.

휘몰아치는 바람에는 스며든 피비린내가 콧속 깊숙이 파고들고, 쉴 새 없이 울려 퍼지는 강철의 소음은 차갑게 식어 있던 피를 끓어 오르게 만들었다.

“고맙다. 지금까지 잘 버텨 주어서.”

전신을 스쳐 지나가는 바람에 묻혀 흐릿해지는 뇌까림.

거구의 노인은 진심을 담아 입을 열었다. 가장 어려운 상황 속에서, 한 치의 물러섬도 없이 싸워 준 그들을 향해.

지금 이 순간에도 강대한 적군에게 필사적으로 맞서고 있는 저들을 향해.

그는 경의와 감사, 그리고 미안함을 표했다.

“한 깃발 아래에서 함께 하기를 맹세했으나, 제 울타리가 무너지는 것이 두려워 이웃의 위기를 외면한 이들이 있다.”

거센 말발굽 사이로 또렷하게 울려 퍼진 음성.

그것은 노인이 스스로에게 되새기는 부끄러움이자, 자신의 뒤를 쫓아 내달리는 모두를 향해 던지는 질타였다.

“쏟아진 물은 주워 담을 수 없고, 시위를 떠난 화살은 되돌릴 수 없는 법. 허나…….”

태원진가는, 산서인들은 쉽게 꺾이지 않았다.

여전히 이곳에서 무수한 목숨을 장작 삼아 타오르고 있었다.

그렇기에 그들의 잔은 아직 깨지지 않았고, 적들의 화살은 아직 시위에 걸려 있을 수 있었다.

“저들을 보아라. 그리고 똑똑히 기억해라!”

어느 순간 들불처럼 일어난 외침이 밤공기를 찢는다.

노인은 치열한 전투가 벌어지는 협곡을 가리켰다.

빠르게 가까워지는 언덕 아래, 뿔피리 소리와 함께 자신들을 향해 움직이는 초원의 군세를 아랑곳하지 않고 외침을 이어 나갔다.

“저들은 우리의 이웃이요, 벗이자 전우이며 한 깃발 아래에서 맹세한 동지다. 더불어 본가(本家)가 외면하려 했던 그들이다!”

노인은 부끄러웠다.

산서인들을 외면하려 했던 그의 가문이. 그 한심한 제안에 잠시나마 흔들렸던 자신이.

하지만 노인은 잊지 않았다.

암천이라는 불의에 맞서, 모두 함께 일어나 도탄에 빠진 천하를 구하자 약속했던 지난날의 맹세를.

그렇기에 온 힘을 다해 이곳까지 달려왔다.

그들이 끝까지 버텨 주기를.

자신들이 늦지 않기를 마음속으로 수없이 되뇌며.

그리고 노인의 그 간절한 소망을, 산서인들은 배반하지 않았다.

미안함과 부끄러움에 차마 들어 올릴 수 없었던 깃발을, 다시 한번 전장에 펼칠 수 있는 기회를 주었다.

“너희는 무엇인가!”

맹수의 포효와도 같은 노인의 외침에, 굳게 닫혀 있던 이천여 명의 입술이 동시에 열렸다.

“투사(鬪士)입니다!”

투사.

아주 오래전부터, 이들은 스스로를 무인이 아닌 투사라고 칭해 왔었다.

그들에게 있어 무공이란, 그저 갈고 닦기 위한 것이 아니라 싸우기 위한 도구였으니.

“너희에게 있어, 적이란 무엇인가!”

다시 한번 토해 낸 노인의 물음에, 어둠 너머에서 나아가던 이들의 눈동자가 번뜩였다.

“투사의 창칼 앞에 무릎 꿇을, 나약한 패자(敗者)입니다!”

두두두두!

부우우!

천둥 같은 말발굽 소리와 연이어 울려 퍼지는 뿔피리 소리.

불과 백여 장 밖, 희뿌연 먼지구름을 일으키며 마주 달려오는 수많은 인마의 모습에도 누구 하나 동요하지 않았다.

그들은 용맹한 투사였고, 저들은 곧 무참히 꺾이고 부러질 패자였으니까.

“마지막으로 묻겠다!”

노인은 부르짖었다. 어느새 그의 손에 들린 거대한 대도(大刀)가 휘황한 섬광을 흩뿌리고 있었다.

“우리는! 누구인가!”

적과의 거리가 좁혀진다. 어둠 속에서 번뜩이는 돌격창의 파도를 바라보며, 이천여 명의 투사들은 한 목소리로 외쳤다.

“하북(河北)의 주인입니다!”

바로 그 순간.

펄럭.

지난 며칠 동안 오직 이 순간만을 기다려온 이십여 명의 기수는 힘차게 깃발을 들어 올렸다.

당장이라도 살아 움직일 것 같은 푸른 호랑이와 거친 필체로 수놓아진 네 글자가, 몰아치는 바람을 타고 맹렬하게 나부꼈다.

마침내 이 전장의 모두를 향해 자신들의 존재를 드러냈다.

하북팽가(河北彭家).

북방의 호랑이. 천하 오대세가의 일좌.

그리고 모두의 앞에서 그들을 이끄는 거구의 노인은, 기나긴 세월을 거쳐 더욱더 강해진 대호(大虎)였다.

“쳐라-!”

땅과 하늘을 떨어 울리는 노호성과 함께, 말안장을 박찬 노인은 코앞까지 들이닥친 수많은 적을 향해 쏘아졌다.

우르르릉.

듣는 이로 하여금 몸과 마음을 얼어붙게 하는 천둥소리.

노인. 아니, 벽력도왕(霹靂刀王)의 대도가 한 줄기의 거대한 벼락이 되어 빽빽한 창칼의 숲을 휩쓸었다.

콰아아앙!

아득한 섬광과 굉음이 사방을 집어삼킨다.

미친 듯이 날뛰며 진형을 붕괴시킨 늙은 호랑이의 뒤로, 짙은 피 안개를 해치며 나타난 이천여 명의 투사들이 하나의 송곳이 되어 적진을 갈랐다.

콰드드득!

새들마저 잠든 깊은 밤.

이 전투는, 중양절(重陽節)은 아직 끝나지 않았다.



* * *



모두가 들었다.

그리고 모두가 보았다.

하늘이 아닌 지상에서 울려 퍼진, 이질적인 천둥소리를.

굉음과 함께 번뜩이는 섬광 너머, 피를 머금고 펄럭이는 수십여 개의 깃발과 적들이 내지르는 새된 비명을.

“하북팽가! 하북팽가다!”

“벼, 벽력도왕……!”

전자는 기쁨에 찬 산서인들의 외침이었고, 후자는 유목민들의 탄식이었다.

벽력도왕 팽철후.

그 별호와 이름은 결코 구시대의 유물 따위가 아니다.

무리 안의 늙은 호랑이는 힘과 지위를 잃는 법이지만, 벽력도왕이라 불리는 대호의 이빨과 발톱은 더욱더 날카로워졌으니까.

더군다나 하북팽가는 모용세가와 더불어 북방을 호령하는 명문 세가.

그런 의미에서 벽력도왕과 그를 따르는 하북의 무인들은, 십왕(十王)과 천하 오대세가라는 칭호를 어떻게 얻을 수 있었는지 똑똑히 보여 주고 있었다.

부우, 부우우우!

쉼 없이 울려 퍼지는 뿔피리 소리를 들으며, 자무카는 문득 생각했다.

‘긴 밤이 되겠군.’

그러나 당황하지는 않았다.

태원진가를 중심으로 뭉친 산서인들의 분전은 예상했던 것 이상이었으나, 하북팽가의 지원은 생각했던 범위 안에 존재하는 것이었으니까.

물론, 벽력도왕의 존재 역시도.

“역시, 그분의 말씀이 맞았군.”

혼잣말처럼 흘러나온 자무카의 한 마디에, 감정에 휩쓸리지 않기 위해 마음을 다잡고 있던 진무경의 얼굴이 굳었다.

“지금, 뭐라고?”

“벽력도왕은 워낙 불같은 성정이라 뒷일을 생각하지 않고 움직일 터. 그러니 혹여 그가 하북팽가를 이끌고 산서를 돕는다 해도 놀라운 일은 아니다.”

막힘없이 말을 이어 가던 자무카가 나직이 덧붙였다.

“라고, 하셨었지. 분명히.”

“……!”

“그런 표정 짓지 말게. 만약 우리가 고작 이 정도도 예상치 못했을 거라 생각했다면, 자네에게 크게 실망하게 될 것 같거든.”

“우……리?”

“그래, 우리.”

작게 고개를 끄덕인 자무카가 진무경을 바라보며 혀를 찼다.

“안타깝군. 내 손을 잡았다면, 자네도 그 ‘우리’에 포함될 수 있었을 텐데.”

저벅.

자무카가 산보하듯이 걸음을 옮긴 그 순간.

슈확!

그의 손에 들린 한 자루의 신월도(新月刀)가 공간을 갈랐다.

소름이 끼칠 만큼 정확하고도 쾌속한 일격 앞에, 진무경은 눈을 부릅뜨며 몸을 비틀었다.

서걱!

머리카락이 흩날린다. 압력만으로도 베어 나간 이마의 상흔에서 흩뿌려진 피가 진무경의 눈 앞을 가렸다.

‘큭.’

진무경의 신형이 일순간 덜컥 굳었다. 지난 이 년간의 수련으로 시야가 차단된 것은 문제가 아니었으나, 눈동자에 닿은 핏물은 그의 평정심을 흐트러트리기에 충분했다.

더불어 그것은, 자무카에게 있어 완벽한 기회이기도 했다.

아직 완성되지 않은, 그러나 커다란 가능성을 품고 있는 젊은 검귀(劍鬼)를 뿌리채 뽑아낼 수 있는 기회.

“그 손으로 직접 목줄을 찼다면, 이런 일은 없었을 텐데.”

자무카는 나직한 음성과 함께 신월도를 들어 올렸다.

냉정함도, 일신의 무위도.

모든 면에서 마조보다 뛰어난 그는 지칠 대로 지쳐 있는 진무경을 상대로도 방심하지 않았다.

그저 침착하면서도 묵묵하게, 가장 빠르고 정확한 궤적을 찾아내어 검을 내리그을 뿐이었다.

‘잘 가게, 젊은 검귀여.’

그리고 매끄러운 도신을 타고 청녹색 강기(罡氣)가 공간을 베어 가르려던 그 순간.

쐐액! 후우웅!

무시무시한 파공음과 함께, 한 줄기 벼락처럼 날아든 대도(大刀)가 자무카와 진무경의 사이를 정확하게 가르며 내리꽂혔다.

꽈아아앙!

하늘이 쪼개지는 듯한 굉음과 희뿌옇게 솟아오르는 먼지구름 너머, 어느새 나타난 거구의 노인이 자무카를 향해 이를 드러내며 웃었다.

“뒈질 준비는 되었느냐?”

전신이 피에 흠뻑 젖은 벽력도왕의 모습에, 자무카가 매끄러운 한어(漢語)로 대답했다.

“고맙군. 내가 할 말을 대신해 줘서.”

자무카에게 있어, 달라지는 것은 없었다.

아무것도.
```

## Final English reading copy

```markdown
# Chapter 965

*Boooo! Boooooo!*

The horns echoed in wave after wave, but their sound was quite different from before.

What should have joined into one great roar was breaking off in fits and starts, and there was even a hint of urgency in it.

So even the people of Shanxi, who didn’t know exactly what the horns meant, could sense that something unexpected had happened to the enemy before them.

And they could sense, too, that this unforeseen turn might bring them a stroke of luck they’d never imagined.

“Now! Now’s our chance!”

“Don’t fall back! Keep pressing them!”

At this moment, not one person among the people of Shanxi wondered what had happened.

Not a single one.

They had all already steeled themselves to die. They had stayed here to protect their homes, their families, and their friends, and were facing the invaders head-on.

Those who came to take, and those who stayed to protect.

The depth of their desperation was different. So was the weight of their resolve.

The people of Shanxi summoned every last ounce of strength, took unsteady steps, and swung weapons that felt heavier than ever.

At the enemies who had faltered, realizing what the horns meant.

At the cruel invaders from the steppe.

*Klang!*

*Thud, thud!*

Sparks burst from the clash of sharp blades.

The Keshiks, frozen in confusion, rushed to fight back. But that moment of distraction gave the Shanxi defenders, burning with fury, their opening.

*Shhk!*

Saber Force surged along a crescent saber, sending limbs flying from three or four men. Yet even as they writhed in agony, the wounded men whose lives still clung to them threw themselves at a Keshik squad leader with all their strength.

“Y-you crazy bastards…!”

*Crack!*

A sickening sound of flesh splitting. The shout cut off abruptly.

There weren’t many people who could survive an axe embedded in the crown of their head.

No—there weren’t any.

“That’s what you get for setting your sights on Shanxi Province, you damned barbarian.”

*Ptooey.*

An unknown martial artist spat phlegm onto the squad leader’s corpse, whose eyes were still wide open in death. Then, carefully, he pried the sword from the hand of his comrade, who had fulfilled his final duty and closed his eyes in peace.

In a muffled voice, he said goodbye.

“Rest here a little while. I’ll kill just ten more and be right back.”

He knew the truth.

No—all the people of Shanxi knew.

They might never come back.

They might never meet again in this life.

But knowing that changed nothing.

Nothing but their resolve to fight to the death.

“Yaaaaah!”

A cry like a scream shook the gorge.

It roused the deep night, pierced the resonance pouring from dozens of horns, and kept traveling farther and farther away.

It swept past grass darkened by night and ground packed hard by countless hooves, until at last it reached a host of horsemen cresting a high hill and charging toward the battlefield.

The towering old man at their head smiled as he heard the fierce cry rising from the people of Shanxi.

“Yes. I hear you loud and clear. This old man does—and so do we all.”

*Thud, thud, thud!*

The thunder of pounding hooves shook the earth.

The wind carried the stench of blood deep into their nostrils. The ceaseless clangor of steel made blood that had gone cold begin to boil.

“Thank you. You’ve held out well.”

His mutter faded beneath the wind rushing past his whole body.

The towering old man spoke from the heart, to those who had fought without giving an inch in the worst of circumstances.

To those still desperately facing an overwhelming enemy.

He offered them his respect, his gratitude, and his apology.

“We swore to stand together beneath one banner. But some of us turned away when our neighbors were in danger, afraid our own fence would come crashing down.”

His voice rang clear amid the pounding hooves.

It was a shame he reminded himself of—and a rebuke he cast at everyone racing behind him.

“What’s spilled can’t be poured back into the cup, and an arrow loosed from the bow can’t be called back. But…”

The Jin Family of Taiyuan and the people of Shanxi had not been easily broken.

They were still here, burning like a fire fed by countless lives.

Their cup had not yet shattered, and the enemies’ arrows might still be on the string.

“Look at them. And remember this well!”

A shout, rising suddenly like a wildfire, tore through the night air.

The old man pointed toward the gorge, where a fierce battle was raging.

The steppe army was moving toward them with horns blaring, just below the hill and rapidly drawing closer. He ignored it and continued shouting.

“They are our neighbors, our friends, our comrades-in-arms—people who swore beneath the same banner! And they are the very people our family tried to turn its back on!”

The old man was ashamed.

Ashamed of the family that had tried to abandon the people of Shanxi. Ashamed that he had wavered, if only for a moment, at such a shameful proposal.

But he had not forgotten.

He remembered the vow they had made in days gone by: to rise together against the injustice of Dark Heaven and save a world sunk in misery.

That was why he had ridden here with all his strength.

Over and over, he had prayed they would hold out until the end.

Over and over, he had prayed they would not arrive too late.

And the people of Shanxi had not betrayed his desperate wish.

They had given him another chance to unfurl the banner he had been too ashamed to raise.

“What are you?”

At the old man’s roar, like the bellow of a beast, the tightly shut lips of two thousand men opened as one.

“We are fighters!”

Fighters.

For a very long time, they had called themselves fighters, not martial artists.

To them, martial arts were not something to practice and polish for its own sake. They were tools for battle.

“And what is an enemy to you?”

At the old man’s question, shouted once more, the eyes of those advancing beyond the darkness flashed.

“Weak losers who will kneel before a fighter’s spear and blade!”

*Thud, thud, thud!*

*Boooooo!*

The thunder of hooves and the blare of horns rang out one after another.

The sight of countless horsemen charging toward them through a hazy cloud of dust, just over three hundred yards away, did not shake a single one of them.

They were valiant fighters, and those men were losers soon to be broken and crushed.

“I’ll ask you one last time!”

The old man cried out. The enormous saber in his hand now scattered dazzling flashes of light.

“Who are we!”

The distance to the enemy closed. Looking at the wave of lances glinting in the darkness, the two thousand fighters shouted with one voice:

“We are the masters of Hebei!”

At that very moment—

*Flap.*

The twenty or so standard-bearers, who had waited for this moment and this moment alone for the past several days, raised their flags with all their strength.

A blue tiger that looked ready to leap to life, and four characters stitched in a rough hand, billowed fiercely in the rushing wind.

At last, they revealed themselves to everyone on the battlefield.

The Hebei Peng Family.

The Tiger of the North. One of the Five Great Families of the world.

And the towering old man leading them all was a great tiger, grown even stronger through the long years.

“Charge!”

With a roar that shook earth and sky, the old man kicked off his saddle and shot toward the countless enemies surging right up to him.

*Rrrumble.*

Thunder that froze body and mind.

The old man—no, the Thunderbolt Saber King’s great saber became a massive bolt of lightning, sweeping through the dense forest of spears and blades.

*Kaboom!*

Dazzling light and a deafening boom swallowed everything around them.

Behind the old tiger, who rampaged wildly and shattered the enemy formation, two thousand fighters burst through the thick haze of blood and split the enemy ranks like a single spear.

*Crack!*

In the deep of night, when even the birds slept—

The battle, and the Double Ninth Festival, were not over yet.

* * *

Everyone heard it.

And everyone saw it.

The strange thunder that rang out from the ground, not the sky.

Beyond the dazzling flash that accompanied the boom, dozens of flags flapped, heavy with blood, and the enemy shrieked.

“The Hebei Peng Family! It’s the Hebei Peng Family!”

“T-The Thunderbolt Saber King…!”

The first was the Shanxi defenders’ cry of joy; the second, the nomads’ lament.

Peng Cheolhu, the Thunderbolt Saber King.

His name and title were no relics of a bygone age.

An old tiger in a pack might lose its strength and standing, but the teeth and claws of the great tiger called the Thunderbolt Saber King had only grown sharper.

What’s more, the Hebei Peng Family was a renowned great family that ruled the north alongside the Murong Family.

In that sense, the Thunderbolt Saber King and the martial artists of Hebei following him were showing exactly how they had earned the titles of Ten Kings and one of the Five Great Families.

*Boooo! Boooooo!*

Listening to the horns blaring without pause, Jamukha suddenly thought:

*This is going to be a long night.*

But he wasn’t flustered.

The Shanxi defenders, united around the Jin Family of Taiyuan, had fought harder than he’d expected. But the Hebei Peng Family’s support was still within the range of what he had anticipated.

And so was the Thunderbolt Saber King himself.

“Just as that person said.”

At Jamukha’s words, spoken almost to himself, Jin Mukyung’s face stiffened. He had been trying to steady himself against his own emotions.

“What did you just say?”

“The Thunderbolt Saber King has such a fiery temper that he’ll act without thinking about what comes after. So even if he were to lead the Hebei Peng Family to Shanxi’s aid, it wouldn’t be surprising.”

Jamukha continued smoothly, then added in a low voice:

“That’s what they said. I remember clearly.”

“……!”

“Don’t look at me like that. If you thought we hadn’t anticipated even something this obvious, I’d be very disappointed in you.”

“W-we?”

“Yes. We.”

Jamukha nodded slightly, then clicked his tongue as he looked at Jin Mukyung.

“Too bad. If you’d taken my hand, you could have been part of ‘we,’ too.”

*Step.*

The moment Jamukha began walking as casually as if he were out for a stroll—

*Shwack!*

The crescent saber in his hand cut through the air.

The strike was so precise and swift it made Jin Mukyung’s skin crawl. He widened his eyes and twisted his body aside.

*Shhk!*

His hair fluttered. Blood sprayed from the gash cut into his forehead by the pressure alone, blinding him.

*Damn it.*

Jin Mukyung’s body jerked to a halt for an instant. His two years of training had made losing his sight no problem—but the blood in his eyes was enough to shake his composure.

And for Jamukha, it was the perfect opening.

A chance to uproot the young Sword Demon, still unfinished but full of potential.

“If you’d put that collar on yourself, this wouldn’t have happened.”

Jamukha raised his crescent saber, his voice low.

Calmness, personal martial prowess—

He surpassed the Demon Bird in every respect. Even facing Jin Mukyung, exhausted to the limit, he did not let his guard down.

He simply, steadily and without a word, found the fastest, most precise path and brought his blade down.

*Farewell, young Sword Demon.*

And just as blue-green Force ran along the smooth blade, about to cut through the air—

*Whoosh! Whoom!*

With a fearsome whistle, a great saber shot in like a bolt of lightning and plunged between Jamukha and Jin Mukyung.

*Kaboom!*

Beyond the boom that sounded as though the sky had split and the cloud of dust rising pale in its wake, the towering old man appeared. He bared his teeth in a grin at Jamukha.

“Ready to die?”

Drenched in blood from head to toe, the Thunderbolt Saber King drew a smooth reply from Jamukha, in fluent Chinese.

“Thanks for saying what I was about to.”

Nothing had changed for Jamukha.

Nothing at all.
```
