<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0820.txt",
      "sha256": "9c9a18a072ab7e2ad34cd2024f5de8dbf754ac2856e55e58269c66e5a1a12dff",
      "bytes": 13677
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b280bce09e1d2598dbf67f4d11306e7844fe27217fb0acdb505a6d018f8deb26",
      "bytes": 2314
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "31f232ac7d1be480b318754ea9507b1473c8082a345026eb79b029b69e3211ae",
      "bytes": 226452
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "048a27b999b03f7a118a20a8d43d50fc143042cb9bf8f47c2fe073c6193069a9",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "f7244109bd6125dbbfa0fa2813c0d1ea5912869aa0cd1e30aeae3e1558b22aa1",
      "bytes": 761
    },
    {
      "path": "characters/Michael.md",
      "sha256": "c5216f59100254f9697989f3d80897dddace34d0b1c35b8f9914567d59a9e656",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "0d76024e527b6fa90905441e1d421ba85864a8428301c71d6668273cf907d4de",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4fa6c9051d06392e56b17f47be21312e0edbc2886ae88d6f1631ded27a3360c0",
      "bytes": 249949
    }
  ],
  "estimated_tokens": 9427
}
-->

# Durable State Update — Chapter 820

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
1 and safe_through 820. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 820. Profile updates may replace only one
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
  "chapter": 820,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 820,
    "continuity_sources": [820],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and its regeneration is slow after forcing Blink beyond its normal range.",
    "Jin interfered with the Doppelganger’s extended-range Blink and arrived with it; the attempt cost the Doppelganger dozens of lives to heal and left Jin severely nauseated and weaker than usual.",
    "The Doppelganger is fleeing the battlefield with a small escort; Jin intends to stop the plan it has spent over thirty years building.",
    "Yahya Muhammad Ahmad Bedouin commands the fanatics; roughly ten thousand fanatics, including more than thirty A-rank War Mages, fight the Hunters.",
    "The fanatics nearly countered Magic Johnson’s Fire Storm with Aqua Storm and are using their numbers to pin down Johnson and the Skeleton King.",
    "Choi Minwoo was severely wounded holding the line, passed out after the Skeleton King caught him, and left the Hero’s Sword in the Skeleton King’s hand.",
    "A furious blond man arrived at the Skeleton King’s position; his identity is not stated in this chapter."
  ],
  "continuity_sources": [
    819
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin reach the Doppelganger before it escapes?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 819,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells."
  ],
  "version": 1
}
```

## Exact glossary matches

| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 무함마드 | **Muhammad** | Prophet whose death is referenced in the history of the Islamic world. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 야흐야 | **Yahya** | First element of the commander’s name. |
| 아흐마드 | **Ahmad** | Third element of the commander’s name. |
| 베두인 | **Bedouin** | Final element of the commander’s name. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 819
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 819
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 817
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 819
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃820화



살아 있는 모든 것은 탄생과 동시에 투쟁의 운명을 부여받는다.

인간도, 몬스터도, 자연 혹은 울타리에서 살아가는 동물과 푸른 초목도 마찬가지다.

투쟁의 이유가 생존 그 자체에 있지 않다고 하여도, 목적을 이루기 위해서라면 싸워서 쟁취해야 했다.

그리고 이 절대적인 법칙 속에서, 나 역시 예외일 수는 없었다.

퍼걱!

최소한의 힘. 최소한의 속도.

하지만 그것만으로도 충분하다. 나는 뇌수를 흩뿌리며 쓰러지는 광신도를 뒤로하고 신형을 비틀었다.

슈확!

바람이 갈라진다. 아무것도 없던 허공에서 뚝 떨어져 내린 섬광이 반 뼘 차이로 스쳐 지나간다.

빈틈없이 전신을 감싼 새카만 로브와 터번 사이로, 크게 뜨여진 눈동자가 보였다.

놈의 눈에 비친 백염의 창날도 함께.

푹, 푸확!

목이 솟구친다. 흩뿌려지는 핏물 사이로 또 다른 적들과 오러가 쇄도한다.

사방에서 들이닥치는 날붙이를 바라보며, 나는 피로 끈적하게 젖은 창대를 말아쥐었다.

후우.

숨을 토해 냈다. 세상이 느려진다. 이완된 근육이 풀어지고 창날을 휘감은 불꽃이 일렁였다.

마치 바람에 흩날리는 무언가의 꼬리처럼.

‘화룡일미(火龍一尾).’

불꽃이 솟구친다. 사방에서 번뜩이는 적들의 오러가 어스름한 새벽을 향해 달려가는 어둠을 몰아낸다.

그리고 나는, 부드럽게 전신을 회전시켰다.

쉬이이잉!

청백색의 불꽃이 공간을 가로질렀다. 그 속도는 코앞까지 들이닥친 그 어떤 오러보다도 빨랐고, 누구도 막을 수 없을 만큼 예리했다.

서걱.

서늘한 절삭음과 함께 누군가의 손에 들려있던 한 자루의 검이 기울어졌다.

아니, 움직임을 멈춘 수십여 명의 광신도들의 몸뚱어리에는 이미 희미한 실선이 그어져 있었다.

“큭. 크륵…….”

떨리는 동공. 꺼져 가는 목소리.

하지만 어떤 말과 행동으로도 막을 수 없을 만큼, 죽음은 무자비하게 들이닥쳤다.

푸화아아악!

희미했던 실선 위로 내달린 불꽃이 적들의 생명을 집어삼킨다.

사방에서 뿜어져 나온 짙은 피 안개가 전장에 자욱하게 내리깔린 수증기를 뒤덮었다.

투두두둑!

머리 위로 쏟아져 내리는 피의 비.

동시에 단 한 번의 횡격(橫擊)으로 조각난 인간의 살과 뼈, 장기가 지면을 나뒹굴었다. 이미 앞서 쓰러진 수백의 광신도들이 그러했듯이.

“악……마.”

누군가의 목소리가 귓가에 닿았다. 물론 얼굴도, 이름도 모르는 광신도 중 하나였고, 동시에 죽여야 할 적이기도 했다.

푸슛!

보지도 않고 내뻗은 손을 따라 쏘아진 지풍(指風)과 함께, 익숙한 종소리가 울려 퍼졌다.

띠링.

또 하나의 죽음을 전하는 알림.

사방을 에워싸고 있던 광신도들이 움직임을 멈췄다.

아마도 저들 중 대부분은 지금 눈앞에서 벌어진 광경을 반의반도 이해하지 못했을 것이다.

자신들의 동료가 어떻게 죽었는지. 이 수많은 병력으로도 어째서 내게 상처를 입히지 못하는지.

그리고 그 의문은 죽어서도 해소되지 않을 것이다.

단 한 사람을 제외한다면.

후웅, 쾅!

곧게 뻗은 창날과 초승달처럼 휘어진 도신(刀身)이 부딪친다.

귓가를 먹먹하게 만드는 굉음. 파공성보다 먼저 도달한 공격을 막아 낸 나는 새하얀 시미터(Scimitar)의 칼날 너머로 보이는 노인을 응시했다.

“염병할 노인네. 드디어 기어 나왔냐?”

“사냥감이 지치질 기다렸을 뿐.”

야흐야 무함마드 아흐마드 베두인이라는, 긴 이름을 가진 노인이 대답과 동시에 시미터를 비틀었다.

카가각!

각기 다른 색을 지닌 오러가 부딪치며 번갯불을 피워 올리고, 그 끝에는 작은 폭발이 기다리고 있었다.

꽈앙!

포성(砲聲)과도 같은 굉음과 함께 거대한 충격이 창날을 타고 전해진다.

그 엄청난 힘을 이기지 못해 뒷걸음질 친 나는, 제자리에 우뚝 서 있는 노인의 모습에 한 가지 사실을 깨달았다.

“설마…….”

“이제야 깨달았느냐, 이교도의 왕이여.”

노인의 주름진 입가에 미소가 맺힌다.

나를 향해 겨누어진 시미터의 도신에는 지금껏 드러내지 않았던, 전혀 다른 두 종류의 기운이 공존하고 있었다.

‘마나. 그리고 마력.’

그 두 개의 단어가 머릿속을 스친 순간, 노인의 목소리가 이어졌다.

“나, 야흐야 무함마드 아흐마드 베두인은 신의 선택을 받은 전사다.”

“허.”

나도 모르게 헛웃음이 흘러나왔다.

도플갱어가 키워 낸 것은 미카엘 실베르트 뿐만이 아니었다. 놈은 가장 충성스럽고, 가장 미친 광신도를 선택하여 마력을 다루는 법을 전수한 것이다.

만약 상반된 두 기운을 받아들일 수 있을 만큼 뛰어난 광신도가 더 있었다면, 도플갱어는 반인반마(半人半魔)의 괴물들을 공장처럼 찍어 냈을 것이다.

“제정신이 아니라는 건 처음부터 알고 있었는데…… 이거 진짜 보통 미친 늙은이가 아니었네.”

“그렇게 믿고 싶다면, 그리하여라.”

고개를 저은 노인이 회색빛 눈동자로 나를 바라보았다.

“네놈은 알지 못한다. 신의 선택을 받기 위해 수십, 수백이 죽었지. 하지만 나만은 아니었다.”

“그래서, 당신이 말하는 그 신의 선택이라는 것이 인간과 괴물을 반반 섞으면 되는 거였나? 그럼 시벌 짬짜면도 신의 전사야?”

“위대한 선지자께서 가로되, 몬스터 역시 신의 피조물이며 이 세상의 타락한 인간을 벌하기 위해 내린 재앙이라 하셨다.”

“지랄한다. 누가 들으면 이 세상이 아니라 옆 세상 사는 줄 알겠네. 그 논리면 너희도 타락한 인간 중 하나야. 이 미친 늙은이야.”

“타락했으나 구원의 기회를 받은 자. 결코 공존할 수 없는 두 힘을 이어받은 자. 그것이 바로 나이며, 이는 신께서 선택하신 전사이자 징벌자로다.”

한 마디, 한 마디마다 신앙을 향한 광기(狂氣)가 드러난다.

그러나 미친놈은 스스로가 미친 소리를 하고 있다는 사실을 모른다.

설령 도플갱어가 모든 광신도를 한자리에 모아 놓고 대국민 사과를 진행해도 믿지 않을 것이다.

저들이 가진 믿음은 인생 그 자체이고, 살아가는 이유였으며, 심지어는 사후 세계와도 연결되어 있는 것이었으니까.

그런 광신도들을 향해, 결국 내가 할 수 있는 말은 하나밖에 없었다.

“미친 새끼들. 말 섞는 시간이 아깝다.”

“한 가지만 명심하거라.”

저벅.

노인이 나를 향해 다가온다. 잠시 주춤거리던 광신도들이 다시금 전의를 불태웠다.

“네놈의 발걸음은, 결코 선지자께 닿을 수 없다는 것을.”

“좆 까.”

쉭.

나는 대답과 함께 바람처럼 쏘아졌다.

짧게 주고받은 대화는 치열한 전투로 잠시 과부하가 걸린 신체를 바로 잡는 시간을 제공했고, 전황(戰況)을 파악하기에도 충분했다.

‘팽팽하다. 치열하지만 잘 싸우고 있어.’

저 멀리서 들려오던 헌터들의 함성이 가까워지고 있다.

하지만 열 배가 넘는 수적 열세를 극복하고 전투에서 승리하기 위해서는 머리를 잘라 내야 했다.

그것이 지금 이 순간에도 도망치고 있을 도플갱어를 좇기 전, 내가 해낼 수 있는 최선의 방법이었다.

쐐애액! 퍼걱!

내뻗은 창날이 세 명의 광신도를 관통한 뒤 빠져나온다.

한 치의 망설임도 없이 수하들을 미끼로 던진 노인이 내 목을 향해 시미터를 휘둘렀다.

슈확! 서걱!

허리를 굽힘과 동시에 비켜 나간 검격(劍格)이, 내 등 뒤로 달려들던 광신도들을 조각 냈다.

내 반격을 대비하여 훌쩍 물러난 노인이 냉막한 목소리로 외쳤다.

“저 악마가 위대하신 선지자를 해하려 한다! 목숨을 바쳐 놈을 막아라!”

빌어먹을 늙은이.

비록 광신도 중의 광신도지만, 세월을 통해 익힌 연륜은 보통이 아니다.

노인은 자신의 임무를 정확히 알고 있었고 전투에 열기에도 냉정함을 유지했다.

‘이대로 시간이 지연되면…… 정말 놈을 영영 놓치고 만다.’

나는 사방에서 부나방처럼 달려드는 광신도들을 베어 넘기며 생각했다. 아니, 계산했다.

현재의 내가 발휘할 힘이 어느 정도인지.

어떻게 싸워야 이 전투를 가장 빠르게 끝낼 수 있을지.

마지막으로, 다시 도플갱어를 좇게 되었을 때쯤에는 얼만큼의 여력이 남아 있을지.

그리고 끊이지 않는 핏물과 비명 속에서, 멍청한 생각을 했다는 것을 깨달았다.

‘시바, 내가 언제부터 이런 걸 하나하나 계산했다고.’

어느 날부터였을까. 매 순간이 투쟁이었다.

그럴 때마다 과거를 잊고, 미래는 머릿속에서 지워 내야 했다.

그렇게 해야 살아남을 수 있으니까. 현재에 모든 것을 걸어야 과거를 생각하고 미래로 나아갈 수 있었으니까.

서걱!

등줄기를 타고 뜨거운 통증이 일어난다. 피로에 젖은 몸이 물먹은 솜처럼 무겁게 느껴진다. 크고 작은 톱니바퀴처럼 돌아가며 들이닥치는 무기들이 전신에 상처를 만들어 냈다.

하지만 그 덕분에, 머뭇거리던 몸과 마음이 온전히 깨어났다.

으득.

이를 악물며 고통을 참아낸 나는 정면에서 달려드는 광신도들을 향해 역수(逆手)로 쥔 창을 내쏘았다.

투창을 시도하기에는 좁은 공간이었지만, 내게는 단 한 걸음이면 충분했다.

콰드드득!

피와 살이 분쇄된다. 신앙심마저 잊게 만드는 고통에 놈들이 비명을 내질렀다.

그 사이로 노인의 명령이 울려 퍼졌다.

“지금이다!”

지금? 지금 뭐?

아. 무기?

“그래서, 어쩌라고?”

나는 입술 사이로 흘러들어오는 핏물을 뱉어내며 손을 뻗었다. 효율적인 전투를 위해 아껴 두었던 화염신장(火焰神掌)이 터져 나온다.

빽빽하게 주위를 둘러싼 광신도들이 화염에 휩싸여 쓰러졌다.

끔찍한 고통으로 몸부림치는 그들의 모습에 주춤거리는 기색이 느껴진다.

‘한 번 더.’

화륵, 퍼어어엉!

청백색의 화염이 어둠을 밝힌다. 살을 태우고 그 안의 피와 뼈를 잿더미로 만들었다.

“끄아아아아!”

“흡……!”

바로 그때였다.

그 잔인하고도 눈부신 화형식 앞에서, 자신도 모르게 뒷걸음질 치던 광신도 중 하나의 목이 허공으로 솟구친 것은.

서걱!

뒤늦게 울려 퍼진 절삭음과 함께, 내 눈을 피해 모습을 감추었던 노인이 서늘한 목소리로 명령했다.

“발사.”

쐐애애애액!

수십 줄기의 파공성이 꼬리에 꼬리를 물고 이어진다.

어느새 부쩍 줄어든 광신도들의 사이로, 묵색의 단궁(檀弓)을 든 궁수들의 모습을 발견했을 때는 이미 늦어 있었다.

푸푸푸푹!

“커헉!”

“끅.”

적과 아군을 가리지 않고 쏟아지는 무차별 사격.

내 주위에서 머뭇거리던 광신도들이 볏짚처럼 쓰러졌고, 마나를 머금은 화살은 그들의 몸뚱어리를 관통하며 나를 향해 달려들었다.

쉬익.

유난히도 길게 늘어지는 파공성.

그리고 핏물과 마나에 휩싸인 묵빛 화살촉들.

순간 느려진 세상 속에서, 나는 확신과도 같은 생각을 떠올렸다.

‘이건…… 피할 수 없다.’

물론 절반은 쳐낼 수 있다. 남은 것 중에서도 또 절반은 어떻게든 몸을 비틀어 피할 수 있을 것이다.

하지만 화룡갑의 수복이 끝나지 않을 지금, 어느 정도의 부상을 각오해야 한다는 점은 변하지 않았다.

그런데 어째서일까.

문득 이상한 기분이 들었다.

머리가 내린 판단을, 본능이 거부하는 듯한 느낌.

그리고 전신의 감각이 내가 모르는 또 다른 영역을 향해 한발 더 나아가는 듯한 기시감.

‘할 수 있다.’

신념과도 같은 기이한 확신이 몸과 마음을 지배한다. 가슴 어림에서 시작된 알 수 없는 간질거림이, 전신을 향해 퍼져 나갔다.

‘바로 지금.’

나는 넋 나간 사람처럼 손을 뻗었다. 코앞까지 도달한 수십 발의 화살을 향해.

아니, 그것들을 감싼 모든 것을 향해.

솨아악.

멈췄던 시간이 흐르기 시작했지만, 그 누구도 입을 열지 않았다.

나는 허공에서 멈춘 화살들을 말없이 바라보다, 손가락을 튕겼다.

스륵.

적을 향해 겨누어진 화살. 그리고 다시 한번 진일보한 중단전(中丹田)의 기운이 공간을 짓눌렀다.

띠링. 띠링. 띠링.

귓가를 파고드는 맑은 종소리를 들으며, 나는 석상처럼 굳어 버린 노인을 향해 웃어 보였다.

“이야, 이게 되네?”

“이, 이게 무……!”

“환불이다, 이 씨벌놈아.”

쉬쉬쉬쉬쉭!

강맹한 파공성이, 이어지려는 목소리를 집어삼켰다.
```

## Final English reading copy

```markdown
# Chapter 820

Everything that lives is born with a destiny of struggle.

Humans, monsters, animals living in the wild or behind fences, even green plants—all the same.

Even when survival itself wasn’t the reason to struggle, you had to fight and take what you wanted.

And under this absolute law, I was no exception.

*Crunch!*

The least force. The least speed.

But that was enough. I twisted away, leaving behind the fanatic collapsing with his brains splattered everywhere.

*Whoosh!*

The air split. A flash dropped from empty space and skimmed past me by half a handspan.

Between the pitch-black robe and turban that covered him completely, I saw his eyes widen. The White Flame’s spearhead was reflected in them.

*Thump. Splurt!*

A head flew up. More enemies and their auras surged through the spraying blood.

Watching blades rush at me from every direction, I tightened my grip on the spear shaft, slick with blood.

*Hoo.*

I breathed out. The world slowed. My relaxed muscles loosened, and the flames coiling around my spearhead flickered.

Like the tail of something caught in the wind.

*Fire Dragon’s Single Tail.*

Flames surged. The enemies’ auras flashing from every direction drove away the darkness racing toward the dim dawn.

And I smoothly spun my whole body.

*Shiiiiing!*

Blue-white flames streaked across the space. They were faster than any aura bearing down on me, sharper than anything anyone could stop.

*Slice.*

With a cool, clean cut, a sword in someone’s hand tilted to one side.

No—faint lines had already appeared across the bodies of dozens of fanatics, frozen in place.

“Ghk. Ghrk…”

Trembling pupils. A fading voice.

But no words or actions could stop death from bearing down without mercy.

*Fwoooooosh!*

Flames raced along the faint lines, devouring the enemies’ lives.

Dense mists of blood spewed in every direction, blanketing the battlefield’s thick, low-lying steam.

*Thud-thud-thud!*

A rain of blood fell from overhead.

At the same time, human flesh, bones, and organs—shattered by a single horizontal strike—tumbled across the ground. Just like the hundreds of fanatics who had fallen before them.

“De…mon…”

Someone’s voice reached my ears. Of course, it belonged to one of the fanatics, someone whose face and name I didn’t know—and an enemy I had to kill.

*Pfft!*

A familiar bell rang as Finger Qi shot from the hand I thrust out without even looking.

*Ding.*

Another notification of death.

The fanatics surrounding me stopped moving.

Most of them probably hadn’t understood even a fraction of what had just happened before their eyes.

How their comrades had died. Why they couldn’t wound me, even with so many fighters.

And those questions would remain unanswered even after they died.

Except for one man.

*Whoom. Boom!*

A straight spearhead collided with the curved blade of a saber shaped like a crescent moon.

The thunderous impact made my ears ring. I blocked the attack before its piercing whistle reached me, then looked at the old man beyond the white scimitar’s blade.

“You lousy old bastard. Finally crawled out, did you?”

“I was waiting for my prey to tire.”

The old man with the long name, Yahya Muhammad Ahmad Bedouin, twisted his scimitar as he answered.

*Ka-ga-gak!*

Auras of different colors collided, sparking like lightning. A small explosion waited at their tips.

*Boom!*

The impact roared like cannon fire and traveled along my spearhead.

Unable to withstand its incredible force, I staggered backward. Seeing the old man standing firm in place, I realized something.

“Don’t tell me…”

“You’ve finally understood, King of the heathens.”

A smile formed on the old man’s wrinkled lips.

Two entirely different energies, never before revealed, coexisted along the scimitar’s blade, still pointed at me.

*Mana. And magical power.*

As those two words crossed my mind, the old man continued.

“I, Yahya Muhammad Ahmad Bedouin, am a warrior chosen by God.”

“Huh.”

A hollow laugh escaped me before I could stop it.

The Doppelganger hadn’t raised only Michael Silbert. It had chosen its most loyal, most insane fanatic and taught him how to wield magical power.

If there had been more fanatics gifted enough to accept two opposing energies, the Doppelganger would’ve churned out half-human, half-demon monsters like they were coming off an assembly line.

“I knew you were out of your mind from the start…but you’re one seriously crazy old bastard.”

“If that is what you wish to believe, then believe it.”

The old man shook his head and looked at me with gray eyes.

“You know nothing. Dozens, hundreds died trying to be chosen by God. But I alone survived.”

“So this ‘chosen by God’ thing you’re talking about just means mixing a human and a monster half and half? Then does that make a half-and-half order of black-bean noodles and spicy seafood noodles God’s warrior too?”

“The great Prophet said that monsters, too, are God’s creations—and calamities sent to punish the fallen humans of this world.”

“Bullshit. Anyone listening would think you lived in some other world, not this one. By your logic, you’re one of those fallen humans too, you crazy old bastard.”

“Though fallen, I was given a chance at salvation. I inherited two powers that can never coexist. That is who I am: a warrior and a punisher chosen by God.”

With every word, the madness in his faith showed through.

But a madman doesn’t know he’s saying crazy things.

Even if the Doppelganger gathered every fanatic in one place and offered a nationally televised apology, they wouldn’t believe it.

Their faith was their entire lives, their reason for living, even something tied to the afterlife.

In the end, there was only one thing I could say to fanatics like that.

“You fucking lunatics. It’s a waste of time talking to you.”

“Remember one thing.”

*Step.*

The old man approached me. The fanatics, who had hesitated for a moment, once again burned with fighting spirit.

“Your steps will never reach the Prophet.”

“Fuck off.”

*Whoosh.*

I shot forward like the wind as I answered.

That brief exchange had given my body a moment to recover from the strain of the fierce battle. It had also been enough to assess the situation.

*It’s even. Fierce, but we’re holding our own.*

The Hunters’ shouts, which had been distant, were drawing closer.

But to overcome a disadvantage of more than ten to one and win this fight, we had to cut off the head.

It was the best I could do before chasing the Doppelganger, which was still fleeing even now.

*Thwack! Crunch!*

My spear pierced through three fanatics and emerged on the other side.

Without a trace of hesitation, the old man used his subordinates as bait and swung his scimitar at my neck.

*Whoosh! Slice!*

I bent at the waist and dodged the slash. It cut apart the fanatics charging at me from behind.

The old man sprang back to prepare for my counterattack and shouted in a cold voice.

“That demon is trying to harm the great Prophet! Stop him with your lives!”

Damn old bastard.

He might’ve been the most fanatical of the fanatics, but the experience he’d gained over the years was no joke.

He knew exactly what his job was, and he stayed cool-headed even in the heat of battle.

*If this drags on any longer…I’ll really lose him for good.*

I thought—or rather, calculated—as I cut down the fanatics charging from every direction like moths to a flame.

How much strength I could bring to bear right now.

How I could end this fight as quickly as possible.

And finally, how much strength I’d have left by the time I could chase the Doppelganger again.

Then, amid the unending blood and screams, I realized I’d been thinking about something stupid.

*When the hell did I start calculating every little thing like this?*

When had it started? Every moment was a struggle.

Whenever that happened, I had to forget the past and erase the future from my mind.

That was how you survived. Only by betting everything on the present could you think about the past and move toward the future.

*Slice!*

A searing pain ran down my back. My exhausted body felt as heavy as a waterlogged cotton blanket. Weapons came at me like big and small gears turning in tandem, leaving wounds all over my body.

But because of that, my hesitant body and mind woke up completely.

*Grit.*

I clenched my teeth against the pain and hurled the spear I held in a reverse grip at the fanatics charging straight at me.

There was barely room to throw a spear, but one step was all I needed.

*Cr-r-runch!*

Flesh and blood were crushed. The pain was enough to make them forget their faith, and they screamed.

The old man’s command rang out among them.

“Now!”

Now? Now what?

Oh. My weapon?

“So what?”

I spat out the blood running between my lips and reached out. The Flame Divine Palm I’d been saving for a more efficient fight erupted.

The fanatics crowding around me went down, engulfed in flames.

I sensed them hesitate at the sight of their comrades writhing in hideous agony.

*One more.*

*Fwoosh—BOOM!*

Blue-white flames lit up the darkness, scorching flesh and turning the blood and bones within to ash.

“Aaaaaagh!”

“Hng…!”

That was when it happened.

One fanatic, who had unconsciously stepped backward before that cruel, dazzling sight of a mass execution by fire, suddenly had his head fly into the air.

*Slice!*

Along with the belated sound of a blade cutting through flesh, the old man—who had vanished from sight to escape my notice—gave a chilly command.

“Fire.”

*Whooooosh!*

Dozens of arrows whistled through the air, one after another.

By the time I spotted the archers with dark-colored bows among the now much thinner ranks of fanatics, it was already too late.

*Thud-thud-thud!*

“Guh!”

“Ghk.”

Indiscriminate fire rained down on friend and foe alike.

The fanatics hesitating around me fell like straw, and the arrows, brimming with mana, pierced their bodies and came straight for me.

*Whoosh.*

An unusually long whistle dragged through the air.

And dark arrowheads, wrapped in blood and mana.

In the moment the world slowed, a thought came to me with absolute certainty.

*I can’t dodge this.*

Of course, I could knock aside half of them. Of the rest, I could somehow twist my body to evade half.

But the Fire Dragon Armor hadn’t finished repairing itself, and that didn’t change the fact that I’d have to take some damage.

But why?

A strange feeling came over me.

It was as if my instincts were rejecting the judgment my mind had made.

And I had a sense of déjà vu, as if my whole body’s awareness were taking another step into a realm I didn’t know existed.

*I can do this.*

A strange certainty, like a conviction, took over my body and mind. An inexplicable tickling sensation began around the center of my chest and spread through my entire body.

*Right now.*

I reached out like a man in a trance, toward the dozens of arrows almost at my face.

No—not just the arrows. Everything around them.

*Shhhhaaa.*

Time began to move again, but no one spoke.

I stared silently at the arrows stopped in midair, then snapped my fingers.

*Swish.*

The arrows pointed toward the enemy. And once again, the power of my newly advanced Middle Dantian pressed down on the space around us.

*Ding. Ding. Ding.*

As the clear chimes pierced my ears, I smiled at the old man, frozen like a statue.

“Whoa. I did it?”

“T-This is—!”

“Refund, you fucking bastard.”

*Whoosh-whoosh-whoosh-whoosh!*

The arrows’ powerful whistle swallowed the words he was about to say.
```
