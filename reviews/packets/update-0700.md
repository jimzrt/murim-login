<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0700.txt",
      "sha256": "2889cfee222deba4434b9b60de80597f6758af6ac8b1154da71b42d22be91e01",
      "bytes": 14356
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ae9a7c8367506cdf20a90aba4bafcfe31db6c0e0b7e883754edbcedc10a02822",
      "bytes": 1931
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b692e6c1c95949375957ebd4a1696a83b8ec456ca92678c22b38b1d7d70fe36b",
      "bytes": 205908
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a171cdff8a4ba238a1c9c2ee78a120b6c6613c7a6f9f8503a6b845dd5c614e75",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "bc7ed69c826e1f54ff59f4de32c1b564bb505c99a7bd0921cb69ada0d13d68d3",
      "bytes": 898
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "246ef743ba833adad091d685695fc1ab29b7a01e6b0a36f937ad801ca02cb60c",
      "bytes": 667
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "5d6a0f298831cf7abf545b4f332f43c8cce1e9ecb98af38817bba3e392e2dfa3",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5a02ded1eebf8b3478e132e1270aeae48417a243d56c3b8f7a7c67d2a945f8a8",
      "bytes": 216186
    }
  ],
  "estimated_tokens": 10764
}
-->

# Durable State Update — Chapter 700

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 700. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 700. Profile updates may replace only one
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
  "chapter": 700,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 700,
    "continuity_sources": [700],
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
    "The demonic qi from the rift is devastating the Inner Palace and overwhelming Nanman's warriors and beasts.",
    "Baeksang has betrayed Nanman while pursuing a decades-old promise from the Southern Heaven Demon Empress.",
    "Baeksang reached his office, found it empty, and broke down after believing the promise had been abandoned.",
    "The office mirror rippled and emitted a dark human figure carrying a Force-infused sword, reviving Baeksang's hope.",
    "The White Tiger leads the beast army in rescuing victims of the demonic qi and carrying them toward the Outer Palace.",
    "Jin Taekyung is severely injured but continues fighting the Southern Heaven Demon Empress.",
    "Jin considers the Southern Heaven Demon Empress stronger than the Western Heaven Demon Lord.",
    "Darkness is descending over the collapsing Inner Palace as the confrontation worsens."
  ],
  "continuity_sources": [
    699
  ],
  "open_questions": [
    "Who or what is the dark figure emerging from Baeksang's mirror, and how does it fulfill the Southern Heaven Demon Empress's promise?",
    "Can Jin Taekyung survive his injuries and stop the Southern Heaven Demon Empress?",
    "Can the White Tiger and the beast army rescue enough victims from the demonic qi?",
    "What will Baeksang do now that the mirror's promise has begun to manifest?"
  ],
  "safe_through": 699,
  "temporary_decisions": [
    "Use mirror for 면경 and do not identify the figure emerging from it until the source confirms its identity.",
    "Use Hwi for 휘 in Baeksang's vocative, while keeping the mirror figure's identity unresolved.",
    "Retain Force for 강기, Finger Qi for 지풍, Internal Injury for 내상, and hellscape for 지옥도.",
    "Preserve Jin Taekyung's first-person voice as conversational, determined, and bluntly profane when describing the Southern Heaven Demon Empress."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 699
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 692
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 696
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature advancing with Jin Taekyung, Yohi, and the beast army.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 699
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, the creator of the massive rift behind Nanman's Inner Palace, and the enemy seeking to seize the Beast King Stone for the Lord of Heaven.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

## Korean source

```text
＃700화



나와 수호령. 그리고 남천마후.

전투가 시작된 지 일각도 채 흐르지 않았지만, 지금까지의 흐름은 잘 쳐 줘서 백중세(伯仲勢)였다.

적어도 지금까지는.

구구구구궁!

“……이런 시발.”

나도 모르게 입 밖으로 튀어나온 욕설.

단지 내궁이 무너져서가 아니다. 남만야수궁의 상징이니 자존심이니 해도, 결국 한낱 건물일 뿐이니까.

문제는 남만야수궁에서도 가장 거대한 건축물이 모래성처럼 허물어지는 동시에, ‘균열’에서 흘러나오던 어둠이 더욱 짙어졌다는 거다.

콰아아아!

마기(魔氣). 다른 이름으로는 마력(魔力).

그 순수하면서도 위험한 기운이 파도가 되어 휘몰아친다.

거대한 먼지구름을 덮고, 공간을 가로질러 아직 내궁을 빠져나지 못한 생명체들에게 닿았다.

“크륵, 커헉!”

- 캬우우우!

인간과 짐승들이 토해 내는 비명.

차츰 초점이 돌아오고 있던 눈동자가 새하얀 흰자위로 물든다. 파르르 경련하던 그들의 몸뚱어리가 섬뜩한 파육음과 함께 꺾이는 것이 똑똑히 보였다.

콰득. 으드득.

죽음이라는 두 글자가 뇌리를 스쳤지만, 아니다.

저들을 기다리는 것은 죽음보다 더한 고통이며, 머지않아 그들에게 찾아올 변화는 고통조차 잊게 만들 것이다.

‘아니, 변화가 아닌 변이(變異)라고 해야겠지.’

모를 수가 없다.

이미 한 번 보았고, 직접 겪어 보기까지 했으니.

균열의 마력은 오백 년 묵은 이무기마저 타락시킬 정도로 강력하다.

비록 수신룡은 홀로 마력을 감당했다는 차이가 있지만, 그렇다 하더라도 평범한 맹수는 물론 어지간한 무림인조차 스스로의 힘으로 마력의 영향을 떨쳐 낼 수 없다.

적어도 누군가 그들을 돕지 않는 한은.

‘그런데 그 누군가가 나네.’

시발 거.

잠시나마 수호령을 홀로 두고 떠나야 한다는 망설임은 잠시뿐이었다.

아직 내궁에는 족히 수천에 달하는 인간과 맹수가 남아 있었다.

그들의 안위도 안위지만, 완전히 마력에 잠식당한 저들이 변이체로 거듭난다면 남천마후가 그린 지옥도(地獄道)가 완성된다.

모든 것을 떠나, 서로를 죽고 죽이는 끔찍한 살육극이 시작되는 것이다.

그리고 찰나라고 부를 수도 없을 만큼 짧은 순간 속, 이런 생각을 떠올린 것은 나 혼자뿐만이 아니었다.

- 가라! 어서!

거의 동시였다.

한줄기 의념(意念)이 머릿속에 울려 퍼진 것과, 내가 땅을 박찬 것은.

쾅!

압축. 그리고 폭발.

전신을 덮치는 거센 바람과 함께 풍경이 뒤바뀐다.

작은 크레이터를 만들며 포탄처럼 쏘아진 신형이 단번에 이십여 장에 달하는 공간을 뛰어넘었다. 부드럽게 지면을 밟는 발끝을 따라 유형화된 기의 불꽃이 일렁인다.

염화일로(炎火一路).

콰아아아!

느려진 세상 속, 청백색의 광염(光焰)이 폭발하듯 터져 나온다.

하늘을 떨어 울리는 포효를 내지르며 남천마후를 향해 달려드는 수호령의 모습도, 살아남은 이들의 최후방에서 전력을 다해 외궁을 빠져나오던 무야호의 모습도 사라진다.

휘우우우.

피비린내가 스며든 바람이 전신을 스쳤다. 어느덧 허공을 밟은 발아래로, 어둠에 휩싸여 몸부림치는 수많은 맹수와 인간들이 보였다.

그리고…….

‘느껴진다.’

초절정의 경지에 오른 뒤, 깨달음을 거듭하며 알게 되었다.

세상 모든 것에는 흐름이 있다는 것을. 육안(肉眼)으로 확인할 수 없다고 해서, 그것을 느끼지 못하는 것은 아니라는 것을.

형체가 없는 바람에도, 강철도 튕겨 내는 단단한 바위에도, 잔잔한 수면에도 존재하는 흐름. 혹은 미약한 틈새.

그것이 바로, ‘결’이다.

‘지금!’

쉬이이익!

나는 확신과 함께 섬전처럼 창을 내리그었다.

투명한 창날 위를 휘감은 삼 갑자의 열양지기가 어둠을 살라 먹고, 공간을 가르며 나아간다.

수천의 생명을 휘감은 캄캄한 어둠 속에 존재하는 결을 베기 위해. 보이지 않는 미세한 흐름을 단숨에 끊어내기 위해.

그리고 다음 순간.

쐐애애액, 꽈앙!

하늘이 쪼개지는 듯한 굉음과 함께, 백염의 창날을 타고 흘러나간 불꽃이 화려하게 폭발했다.

“……!”

나도 모르게 크게 뜨인 눈.

비록 연이은 전투로 인한 피로와 부상의 여파가 남아 있지만, 현재로서는 거의 전력을 다한 일격이었다.

전부는 아니더라도 마기의 일부를 흩어 놓을 수는 있다고 자신했을 만큼.

‘그런데…… 이걸 쳐 내?’

짧은 순간이었지만, 정확히 봤다.

어둠 속에서 빛살처럼 날아온 강기(罡氣)를. 동시에 빛살이라 부르기에는 너무나도 어둡고 불길한 그 힘을.

툭.

부드럽게 지면에 내려앉은 나는 캄캄한 어둠 속을 노려보았다.

아니, 뿌연 먼지구름에 휩싸인 채 허물어진 내궁의 잔해 속에서 천천히 걸어 나오는 흐릿한 인영을.

“……복면? 뭐 하는 새끼냐. 너?”

그리고 내 물음에 돌아온 대답은, 십여 장 너머에서 번뜩인 한 줄기의 섬광이었다.

슈화아아악! 서걱!

그야말로 간발의 차.

번개처럼 고개를 비튼 나는 힐끗 등 뒤를 살폈다. 용케 지금까지 형태를 유지하고 있던 전각이 뭉개지다시피 반으로 갈라져 있었다.

우득, 쿠구궁!

반 박자 늦게 무너지는 전각을 보며, 나는 내심 중얼거렸다.

‘빠르다.’

더불어 정제되지 않은 흉폭한 힘이 느껴진다. 이건 거칠다고도 할 수 있지만, 다른 의미로는 파괴적이라는 뜻도 된다.

단 한 번이라도 피하지 못한다면 시체조차 찾지 못할 만큼.

하지만 그건, 나 역시 마찬가지다.

푹. 쐐애애액!

굳이 인벤토리에서 소환할 필요도 없었다.

사방에 널려 있는 무수한 병장기들. 그중 지면에 꽂혀 있던 철창 하나를 뽑아 역수(逆手)로 쥔 채 힘껏 쏘아 보냈다.

쾅!

강기에 가로막혀 힘없이 튕겨 나가는 철창. 그러나 충분히 예상했던 바다.

진작 철창을 쏘아 보냄과 동시에 신형을 날린 나는, 정체를 알 수 없는 복면인을 향해 백염을 내질렀다.

슈확, 퍼엉!

창날의 끝에서 압축된 공기가 터져 나갔다. 종이 한 장 차이로 몸을 비틀어 공격을 피해 낸 복면인이 창대를 붙잡으며 성큼 걸음을 내디딘다.

동시에 놈의 손끝에서 묵빛 검광(劍光)이 번쩍였다.

서걱!

희미한 통증.

피했으나, 피하지 못했다. 강맹한 검격(劍格)이 불러온 바람에 스친 콧날에서 핏물이 솟구친다.

그러나 이깟 피 몇 방울쯤은 헐값이다. 지금 흘린 피를 대가로 더욱 큰 것을 얻어 낼 테니.

‘나를 다른 무림인들과 같다고 생각했다면, 큰 오산이지.’

무인(武人)들은 자신의 무기를 목숨처럼 여긴다.

대다수가 병장기를 다루는 무공을 익혔고, 어설픈 권장지각으로는 치열한 생사결에서 살아남을 수 없다는 것을 알기 때문이다.

하지만 나는 다르다.

인간의 한계를 벗어난 신체 능력과 더불어 신공(神功)이라 불려도 부족함이 없는 열화문의 권장지각.

그리고 무한에 가까운 수용량을 지닌 인벤토리에는 수많은 병장기가 잠들어 있으니까.

콰득!

제아무리 신병이기(神兵利器)라 해도 적에게 닿지 못한다면 무소용이다.

창대를 놓음과 동시에 검을 쥐고 있는 복면인의 손목을 잡아챈 나는, 번개처럼 나머지 한 손을 뻗었다.

오직 나만이 이해할 수 있는 명령어와 함께.

‘인벤토리 오픈. 소환.’

쉭!

정확히 심장을 노린 일격을 빗나갔지만, 열양지기로 붉게 달아오른 녹슨 비수는 갑옷보다도 단단한 호신강기를 가르며 가슴을 파고들었다.

푸욱!

“……!”

신음조차 흘리지 못한 채 덜컥 굳어 버린 복면인의 몸뚱어리. 그러나 여기에서 멈출 생각은 없었다.

‘확실하게 끝내야 한다.’

복면인의 이름도, 별호도 모르지만 남천마후의 휘하에 있는 놈이라는 건 확실하다.

어설픈 손속으로 더 큰 화를 부르기 전에, 반드시 이 자리에서 숨통을 끊어야 한다.

지금. 이 자리에서.

으득, 콰지직!

여전히 놈의 손목을 붙잡은 채, 섬전처럼 차올린 무릎 끝에서 으스러지는 뼈마디가 느껴진다.

팔꿈치가 박살 난 팔이 축 늘어지며 힘이 풀린 손아귀에서 검 자루가 미끄러지던 그때.

스륵.

까딱, 미세하게 움직인 복면인의 손가락과 함께 보이지 않는 사각(死角)에서 파공성이 일었다.

쉬이이잉!

세상 모든 것에 결과 흐름이 있는 것처럼, 무기가 내는 소리 역시 마찬가지다.

‘뭐지?’

분명 어디선가 들어 본 듯한 소리.

그와 함께 한 줄기 위화감이 뇌리를 스쳤지만, 그 생각을 이어 나갈 시간이 없다.

지금의 내게는 선택을 위한 아주 짧은 찰나의 순간만이 주어졌을 뿐이다.

내 본능과 화룡갑을 믿고 복면인을 완전히 끝낼 것인가. 아니면 이미 극심한 부상을 입었을 복면인을 뒤로하고 우선 내 안위를 지킬 것인가.

이 물러설 수 없는 양자택일(兩者擇一)의 순간 속, 결심을 굳힌 나는 돌아서는 동시에 손을 뻗었다.

아니, 쌍장(雙掌)을 떨쳤다.

복면인. 그리고 코앞까지 들이닥친 두 줄기 섬광을 향해.

퍼엉! 꽝!

화염신장(火焰神掌)에 가슴을 적중당한 복면인의 신형이 포탄처럼 쏘아져 내궁의 잔해에 처박힌다.

하지만…….

콰드드득!

한 번에 두 마리의 토끼를 잡는다는 건 너무 큰 욕심이었을까.

엄청난 충격에 의해 밀려 나가는 몸뚱어리. 깊은 고랑을 만들며 열 걸음을 물러난 후에야 불에 덴 듯한 통증이 찾아왔다.

툭. 투두둑.

손가락을 타고 굴러떨어진 핏물이 지면을 적신다. 살과 근육이 찢어져 반쯤 너덜너덜해진 왼손을 지혈한 나는 입술을 깨물었다.

고통 때문에? 틀렸다. 이 정도의 통증과 부상은 헌터 시절에도 심심찮게 겪었다.

최대한 전력을 보전해야 하는 상황에서 한쪽 손이 다친 건 틀림없는 악재(惡材)지만, 그렇다고 해서 영 쓰지 못할 정도는 아니다.

진짜 문제는 부상과 통증이 아니라, 복면인의 가슴에 화염신장을 격중시킨 순간 느꼈던 어마어마한 반탄력(反彈力)과 파공성만으로 위화감을 불러일으켰던 섬광의 정체였다.

‘이건.’

형태와 크기의 차이가 있을 뿐 아무리 봐도 눈에 익은 무기다.

왼손에 붙잡힌 쌍륜(雙輪)을 응시하던 나는 천천히 몸을 돌렸다.

저승에서 기다리겠다는 말을 유언으로 남긴 어느 노괴를 떠올리면서.

“너, 대설귀랑 무슨 관계냐?”

입을 열면서도 이 물음에 대한 대답이 돌아오지 않길 바랐다. 마지막에 느꼈던 엄청난 반탄력도 그저 나만의 착각이었으면 좋겠다는 생각도 함께.

하지만 불길한 짐작은 이미 현실로 드러나고 있었다.

쿠궁. 파스슥.

아직 가라앉지 않은 먼지구름 속, 육중한 무게의 철근과 목재가 들썩이고 희끄무레한 인영이 우뚝 일어선다.

뒤이어 번뜩이는 섬광이 이십여 장의 공간을 가로지르며 쇄도했다.

쐐액, 콰드드득!

실로 맹렬한 기세.

한껏 공력을 실은 손으로 섬광을 잡아챈 나는 입을 다물었다.

비수다.

조금 전, 이 손으로 직접 한 사람의 가슴에 박아넣었던 바로 그 비수.

녹이 잔뜩 슬어 있는 한 뼘 길이의 도신(刀身)에는 내 것이 아닌 다른 누군가의 핏물이 묻어 있었다. 공격이 성공적이었다는 증거다.

‘그렇다면 분명 치명상을 입었을 텐데…… 도대체 어떻게?’

지긋지긋할 만큼 잘 알고 있다.

인간은, 특히 초절정 고수는 생각보다 쉽게 죽지 않는다는 것 정도는.

그들은 가슴에 비수가 박혀 있더라도 능히 일당백(一當百)을 실천할 수 있는 괴물들이다.

하지만 그 비수를 박아 넣은 자가 그와 비슷한 수준의, 혹은 윗줄의 실력을 지닌 초절정 고수라면 이야기는 달라진다.

‘이건 뒷골목 왈패 간의 싸움이 아니니까.’

고수들 간의 생사결에서 가장 주의해야 할 점은, 날 선 병장기가 아니라 그것에 실린 공력(功力)이다.

상처를 비집고 신체 내부로 흘러 들어가 혈맥을 찢어발기는 공력.

그런 일격에 당하면 제아무리 초절정 고수라 한들 내상을 피할 수 없다.

심지어 뛰어난 무공과 심후한 공력을 지닌 대설귀조차 예외는 아니었다.

그런데…….

‘아무렇지 않게 일어난 것으로도 모자라서, 가슴에 박혀 있던 비수를 뽑아서 던져? 내상을 가라앉히는 것만도 힘든 마당에 이 정도의 공력을 실어서?’

더군다나 비수는 놈이 입은 가장 큰 부상 중 하나였을 뿐이다.

한쪽 팔은 최소 불구. 게다가 마지막에는 화염신장까지 처맞은 놈이다. 설령 십왕(十王) 급의 고수라 해도 저만큼 멀쩡할 수는 없다.

“……너. 도대체 뭐 하는 새끼냐.”

어느덧 전신을 휘감은 위화감. 그리고 서늘한 경계심.

하지만 내 물음에 대한 복면인의 대답보다 한발 앞서, 거대한 굉음이 울려 퍼졌다.

콰아아앙!

지면에 유성처럼 내리꽂힌 은빛 신형.

상처투성이가 된 몸으로 숨을 헐떡이는 수호령의 머리 위 허공에는 미소를 띤 남천마후가 우뚝 서 있었다.

“내 사냥개란다. 아주 공들여 길들인.”
```

## Final English reading copy

```markdown
# Chapter 700

Me, the Guardian Spirit, and the Southern Heaven Demon Empress.

Less than fifteen minutes had passed since the battle began, but so far, the best way to describe its flow was that we were evenly matched.

At least, until now.

Rumble, rumble, rumble!

“……For fuck’s sake.”

The curse slipped out of my mouth before I could stop it.

Not simply because the Inner Palace was collapsing. No matter how much it symbolized the Nanman Beast Palace and its pride, it was still just a building in the end.

The problem was that, at the same time the largest structure in the Nanman Beast Palace was crumbling like a sandcastle, the darkness flowing from the rift had grown even thicker.

Kraaaaaash!

Demonic qi. Also known as magical power.

That pure yet dangerous energy surged like a wave.

It covered the enormous cloud of dust, crossed the space, and reached the living beings that had not yet escaped the Inner Palace.

“Grrk, keugh!”

—Kyaaaaaa!

The screams of humans and beasts poured forth.

Their eyes, which had gradually begun to regain focus, flooded with white. Their trembling bodies twisted sharply with sickening sounds of splitting flesh.

Crack. Crrrunch.

The word *death* flashed through my mind, but no.

What awaited them was pain worse than death, and the changes that would soon come over them would make them forget even the pain.

*No. I should call it mutation, not change.*

There was no way I could fail to recognize it.

I had already seen it once. I had even experienced it firsthand.

The magical power from the rift was strong enough to corrupt a five-hundred-year-old imugi.

The Water God Dragon had endured the magical power alone, which made its situation different. Even so, ordinary beasts—and even most martial artists—could not shake off its influence through their own strength.

At least, not unless someone helped them.

*And apparently, that someone is me.*

For fuck’s sake.

My hesitation at having to leave the guardian spirit alone had lasted only a moment.

There were still several thousand humans and beasts left inside the Inner Palace.

Their safety was reason enough, but if those who had been completely consumed by the magical power became mutants, the hellscape the Southern Heaven Demon Empress had envisioned would be complete.

Putting everything else aside, a horrific slaughter would begin, with them killing one another over and over.

And in that moment—too brief to even be called an instant—I was not the only one to reach that conclusion.

—Go! Hurry!

It happened almost simultaneously.

The instant a single thought rang inside my head, I kicked off the ground.

Boom!

Compression. Then explosion.

The scenery changed along with the violent wind that swept over my entire body.

My body shot forward like a cannonball, creating a small crater as I crossed more than sixty yards in one bound. Flames of manifested qi shimmered beneath my toes as they touched the ground softly.

Flamefire Path.

Kraaaaaash!

In the slowed world, blue-white light-flames burst out like an explosion.

The guardian spirit charging toward the Southern Heaven Demon Empress with a roar that shook the heavens vanished from sight.

So did Muyaho, racing out of the Outer Palace with all his strength at the very rear of the survivors.

Whoooosh.

Wind carrying the scent of blood brushed across my entire body. By then, beneath the feet I had planted in midair, I could see countless beasts and humans writhing as darkness engulfed them.

And……

*I can feel it.*

After reaching the Supreme Peak realm and gaining insight again and again, I had come to understand.

Everything in the world had a flow. The fact that something could not be confirmed with the naked eye did not mean it could not be felt.

There was a flow—or perhaps a faint gap—in the formless wind, in solid rock that could repel steel, and on calm water.

That was the grain.

*Now!*

Fwoooosh!

With absolute certainty, I slashed my spear downward like a flash of lightning.

Three jiazi of Scorching Yang Qi coiled around the transparent spearhead, consuming the darkness as it cut through space.

I was cutting the grain within the pitch-black darkness that had wrapped around thousands of lives.

Severing the invisible, microscopic flow in a single stroke.

And then.

Whoooosh—boom!

With a roar that seemed to split the sky, the flames flowing along the White Flame spearhead exploded magnificently.

“……!”

My eyes widened before I knew it.

Despite the fatigue and injuries left by the battles I had fought one after another, this attack had been nearly full force.

I had been confident that, even if I could not disperse all of the demonic qi, I could at least scatter some of it.

*But…… it knocked this away?*

It had been only a brief moment, but I had seen it clearly.

The Force that flew from the darkness like a ray of light.

At the same time, it was far too dark and ominous to be called a ray of light.

Tap.

I landed gently on the ground and glared into the pitch-black darkness.

No—the hazy figure slowly walking out from the ruins of the Inner Palace, shrouded in a cloud of dust.

“……A mask? What the fuck are you supposed to be?”

The answer to my question was a single flash of light that glinted from more than thirty yards away.

Shwaaaak! Slash!

It was a matter of a hair’s breadth.

I twisted my head like lightning and glanced over my shoulder. A pavilion that had somehow retained its shape until now had been crushed and split in half.

Crack. Rumble!

Watching the pavilion collapse half a beat late, I muttered inwardly.

*Fast.*

I could also sense an unrefined, savage power.

That could be called rough, but in another sense, it meant destructive.

If I failed to evade it even once, there would not be enough of my corpse left to find.

But the same was true of me.

Thrust. Whoooosh!

There was no need to summon a weapon from my Inventory.

Countless weapons were scattered all around us. I pulled an iron spear from the ground, gripped it in reverse, and hurled it with all my strength.

Boom!

The iron spear was blocked by Force and bounced away helplessly.

But I had expected that.

The moment I sent the spear flying, I had launched my body forward as well. I thrust White Flame toward the masked man whose identity I did not know.

Shu-whoom! Boom!

Compressed air burst from the tip of the spear.

The masked man twisted his body by the width of a sheet of paper and evaded the attack, then grabbed the shaft and took a large step forward.

At the same time, dark sword-light flashed from his fingertips.

Slash!

A faint pain.

I had dodged, but not completely. Blood sprang from the bridge of my nose, grazed by the wind created by that powerful sword strike.

But a few drops of blood were a cheap price.

I would obtain something much greater in exchange for the blood I had shed just now.

*If you thought I was like other martial artists, you made a serious mistake.*

Martial artists treated their weapons like their lives.

Most of them had learned martial arts that involved weapons, and they knew that clumsy fist, palm, finger, and kicking techniques could not carry them through a fierce life-and-death duel.

But I was different.

Along with physical abilities that surpassed human limits, I possessed the Fire Gate Clan’s fist, palm, finger, and kicking techniques—martial arts so magnificent that calling them divine arts would not be enough.

And my Inventory, which possessed a capacity close to infinite, held countless weapons.

Crack!

No matter how divine or powerful a weapon was, it was useless if it could not reach the enemy.

The moment I released the spear shaft, I seized the wrist of the masked man holding the sword and thrust out my other hand like lightning.

Along with a command only I could understand.

*Inventory open. Summon.*

Whoosh!

The strike missed its mark—the heart—but the rusty dagger, glowing red from the Scorching Yang Qi, cut through a Body-Protecting Qi barrier harder than armor and drove into his chest.

Puhk!

“……!”

The masked man’s body went rigid without even being able to groan.

But I had no intention of stopping there.

*I have to finish this properly.*

I did not know the masked man’s name or sobriquet, but one thing was certain: he was under the Southern Heaven Demon Empress.

Before half measures brought about an even greater disaster, I had to snuff out his life right here.

Now. In this place.

Crack! Crunch!

Still gripping his wrist, I felt bones shatter beneath the tip of my knee as I drove it up like a flash of lightning.

His arm, with its elbow crushed, hung limply. As the strength left his hand, the sword hilt began to slip from his grasp.

Srrk.

At that moment, the masked man’s fingers moved ever so slightly, and a sound of something breaking through the air rang out from an invisible blind spot.

Whoooosh!

Just as everything in the world possessed its own grain and flow, the same was true of the sounds made by weapons.

*What is that?*

It was definitely a sound I had heard somewhere before.

A sense of incongruity flashed through my mind along with it, but I had no time to follow the thought any further.

I had only the briefest instant to make my choice.

Should I trust my instincts and the Fire Dragon Armor and finish off the masked man completely?

Or should I abandon the masked man, who had already suffered grievous injuries, and protect myself first?

At that moment of an irreversible either-or choice, I hardened my resolve and turned around while thrusting out my hands.

No.

I swung both palms.

Toward the masked man—and the two streaks of light that had rushed right up to my face.

Boom! Crash!

The masked man’s body, struck in the chest by the Flame Divine Palm, shot away like a cannonball and slammed into the ruins of the Inner Palace.

But……

Crrrunch!

Had trying to kill two birds with one stone been too greedy?

My body was forced backward by the tremendous impact. Only after retreating ten steps and carving deep furrows into the ground did I feel the pain, as though I had been burned.

Tap. Drip-drip.

Blood rolled down my fingers and fell to the ground.

After staunching the wound in my left hand, where flesh and muscle had been torn apart and left hanging in tatters, I bit down on my lip.

Was it because of the pain?

Wrong.

I had suffered pain and injuries like this plenty of times back when I was a Hunter.

Having one hand injured while I needed to conserve as much of my strength as possible was certainly a setback, but it was not so bad that I could not use the hand at all.

The real problem was not the injury or the pain.

It was the tremendous rebound force I had felt when my Flame Divine Palm struck the masked man’s chest—and the identity of the flash whose sound alone had caused that sense of incongruity.

*This is……*

The form and size were different, but there was no mistaking it.

It was a weapon I knew all too well.

I stared at the twin wheels clutched in my left hand and slowly turned around.

I thought of the old fiend who had left behind the words that he would be waiting for me in the afterlife.

“What’s your relationship with the Great Snow Fiend?”

Even as I opened my mouth, I hoped I would not receive an answer.

I also hoped the tremendous rebound force I had felt at the very end had merely been my imagination.

But my ominous suspicion had already become reality.

Rumble. Rustle.

Within the cloud of dust that had yet to settle, heavy rebar and timber shifted, and a pale figure rose to its feet.

Then a flashing streak of light crossed more than sixty yards and hurtled at me.

Whoosh! Crrrunch!

Its momentum was truly ferocious.

I caught the streak of light with a hand packed with internal energy and fell silent.

It was a dagger.

The very dagger I had driven into a man’s chest with this hand only moments ago.

Blood that was not mine stained the heavily rusted blade, which was about a handspan long.

Proof that my attack had succeeded.

*If so, he should have suffered a fatal wound…… How the hell?*

I knew this all too well—almost to the point of disgust.

Humans, especially Supreme Peak masters, did not die as easily as one might think.

They were monsters capable of fighting a hundred men alone even with a dagger buried in their chest.

But the situation changed when the person who had driven in that dagger was a Supreme Peak master of similar or greater ability.

*This isn’t a fight between street thugs.*

In a life-and-death duel between masters, the thing one had to be most wary of was not the sharp weapon itself, but the internal energy carried by it.

Internal energy that forced its way through a wound and tore apart the blood vessels inside the body.

Even the greatest Supreme Peak master could not avoid Internal Injury after suffering such an attack.

Even the Great Snow Fiend, who possessed superb martial arts and profound internal energy, had not been an exception.

And yet……

*Not only did he get up as if nothing had happened—he pulled out the dagger lodged in his chest and threw it? While it should have been difficult enough just to suppress his Internal Injury, he even put this much internal energy into it?*

Besides, the dagger was only one of the most serious injuries he had suffered.

One arm was crippled at the very least. And then he had taken a direct hit from the Flame Divine Palm.

Even a master at the level of the Ten Kings could not be that unharmed.

“……You. What the hell are you?”

A sense of incongruity had wrapped itself around my entire body by then, along with a chilly wariness.

But before the masked man could answer my question, a tremendous roar rang out.

Kraaa-boom!

A silver figure slammed into the ground like a meteor.

The guardian spirit, its body covered in wounds, gasped for breath.

And above its head in midair, the Southern Heaven Demon Empress stood with a smile.

“He’s my hunting dog. One I trained with a great deal of care.”
```
