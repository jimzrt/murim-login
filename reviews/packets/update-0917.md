<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0917.txt",
      "sha256": "d0757855c55f5750b112408b0fd82226da3937f490d823144ae8649d39edbe0b",
      "bytes": 13403
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b20a4b2b96cf6bf3ce53f2152a0865c7e2904b7197cd945ea87133105b298386",
      "bytes": 853
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "56d1a46d630cf4aa4e3a0007472e11191fdc88c9195c4f7ccf28d51fb0617cf6",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "0935411ab3abeedc5d2d6b1942c6b3e7150ba51ae6bfa6e603669cae620a1e21",
      "bytes": 731
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "892c7549a92d864fcb9a226c8eaf8425ba99bf5af082be0b867136f236c36734",
      "bytes": 1242
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "dc9262815490f22cf21b53f6379b1c522f6cec4b70d522c78cb4296dae3a68cd",
      "bytes": 752
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0ef5ac19c7cf2173a38979e7f71123400b2d1b27bc13ad8e05dbbb1a88a39957",
      "bytes": 264640
    }
  ],
  "estimated_tokens": 9681
}
-->

# Durable State Update — Chapter 917

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
1 and safe_through 917. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 917. Profile updates may replace only one
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
  "chapter": 917,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 917,
    "continuity_sources": [917],
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
    "Jin Taekyung is critically injured after saving Jeok Cheongang and appeals to the System; a chime sounds in response.",
    "Jeok Cheongang has unleashed immense white fire against the Eastern Heaven Demon Lord; Golden Ox Palace was engulfed by it.",
    "The Eastern Heaven Demon Lord is shielding himself with death energy and continues his revenge."
  ],
  "continuity_sources": [
    915,
    916
  ],
  "open_questions": [
    "What does the System’s chime signal, and will it help Taekyung survive?",
    "Can Taekyung survive his injuries?",
    "Can Jeok Cheongang defeat the Eastern Heaven Demon Lord?",
    "What is So Gyo’s identity and allegiance?"
  ],
  "safe_through": 916,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 916
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 916
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a being no longer human, a former Maoshan Sect disciple who commands the dead with a bell.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 916
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts and cherishes Jin Taekyung, his publicly acknowledged second Disciple and intended heir, and Taekyung risks his life to protect him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 910
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
＃917화



화아악.

거센 광풍이 휘몰아친다. 지면에 켜켜이 쌓여 있던 새카만 잿가루가, 아직 꺼지지 않는 불씨가 바람을 타고 온 사방에 흩날렸다.

그리고 모두의 시야를 차단한 그 희뿌연 장막 속에서, 화염을 머금은 일권(一拳)이 공간을 갈랐다.

퍼엉, 콰아아아!

압축된 공기가 터져 나간다. 달구어진 공기 너머로 백색 화염이 넘실거렸다.

그것은 그 무엇으로도 막을 수 없는 불길이었다.

용의 숨결이었고, 포효였으며, 가늠할 수 없을 만큼 거대한 분노였다.

감히 자신의 역린(逆鱗)을 건드린 적들을 향해 쏟아지는 늙은 용의 화염은, 그 어느 때보다 맹렬하게 타올랐다.

이미 불멸(不滅)에 가까운 존재로 거듭난 누군가가 자신도 모르게 죽음이라는 단어를 떠올릴 만큼.

‘아.’

동천마군은 내심 침음성을 흘렸다.

어느덧 두려움과 경탄이 뒤섞인 회색빛 눈동자는 끊임없이 화염을 쏟아내며 다가오는 한 사람을 향하고 있었다.

화왕(火王) 적천강.

바로 그였다.

오직 그였다.

저 드높은 하늘에 닿지 못했던 열 명의 왕.

그중에서도 가장 앞선 불의 제왕(帝王)이 비로소 숨겨 두었던 날개를 펼쳐 솟아오르고 있었다.

무신이라는 하늘을 장식한 세 개의 별들을 향해.

건드려서는 안 될 것을 건드린, 자신의 적들을 향한 분노를 토해 내며.

드드득!

전신을 두드리는 거대한 충격.

미증유의 힘이 실린 일장(一掌)에 동천마군의 주위를 빈틈없이 에워싸고 있던 죽음의 기운이 뒤흔들린다.

만근의 힘으로 지면에 틀어박힌 두 다리가 깊은 고랑을 만들어 내며 밀려났다.

쾅! 쾅! 콰아앙!

나아가는 자.

그리고 물러날 수밖에 없는 자.

적천강이 전자라면 동천마군은 후자였다.

마치 신벌(神罰)처럼 쉴 새 없이 떨어지는 벼락을 피해 한껏 몸을 웅크린 죄인이었다.

‘어떻게, 도대체 어떻게…….’

이미 크고 작은 상처가 가득한 저 지친 육신으로 어찌 이토록 강한 힘을 낼 수 있단 말인가.

저토록 분노할 수 있단 말인가.

동천마군은 혀끝에서 감도는 탄식을 삼켰다.

그리고 압도적인 기세를 흩뿌리며 다가오는 적천강을, 손을 뻗으면 만져질 것만 같은 그의 극렬한 분노를 이해하는 자신을 발견했다.

그 또한 마찬가지였으니까.

쾅!

가족을 잃고.

콰앙!

사문을 잃었다.

콰아앙!

그렇게 모든 것을 잃었다고 생각한 그때, 텅 비어 버린 자신의 마음 한구석에 남아있던 무언가를 발견했다.

‘분노.’

희로애락(喜怒哀樂)을 느낄 수 있기에 인간이라고 했다.

웃고, 분노하고, 슬퍼하며, 즐길 수 있기에 생명이라고 했다.

그러나 동천마군은 그중 셋을 잃어버렸다.

남아 있는 것이 오직 분노뿐이었기에, 마침내 스스로 인간을 포기한 괴물이 되었다.

복수귀(復讎鬼)라는 이름의 괴물이.

그렇기에 한편으로는 적천강을, 생사의 갈림길에 선 제자를 본 늙은 스승의 마음을 이해했다.

자신이 온 힘을 다해 일으킨 죽음의 기운마저 불사르려 하는 저 강대한 화염에 담긴 분노 역시도.

콰아아아앙!

그 순간.

동천마군은 느낄 수 있었다.

그를 둥글게 에워싸고 있던 죽음의 기운이 마침내 한계에 다다랐다는 것을.

지금 이 순간만큼은 적천강의 분노가, 자신의 분노를 넘어섰다는 것을.

쩌적.

균열을 알리는 그 소리가 동천마군의 귓가에 닿았다. 그의 몸 깊숙한 곳에서 끊임없이 흘러나오던 기운이 흩어지고 있었다.

그리고 그 균열의 시작점에 새하얀 광염(光焰)이 깃든 주먹이, 최후의 보루를 무너트리는 화염과 그보다 더한 열기를 줄기줄기 쏟아 내는 두 눈동자가 있었다.

“똑똑히 깨달아라.”

그저 마주한 것만으로도 잿더미가 되어 버릴 듯한 안광.

“네놈이 무엇을 건드렸는지.”

그러나 흘러나오는 목소리는 북해의 빙하처럼 차갑다. 동천마군의 등골을 얼리고 영혼에 스며들었다.

그가 죽음을 딛고 일어선 그날부터 오랫동안 잊고 있던 공포를 깨웠다.

‘허.’

동천마군은 자신도 모르게 몸을 떨었다. 실소를 흘렸다.

그리고 불현듯 깨달았다.

‘어쩌면 삼성(三星), 그 이상.’

적어도 지금 이 순간만큼은, 늙은 용의 분노를 막을 수 있는 것은 아무것도 없었다.

아무것도.

콰창!

마침내 갈라지고, 깨져 나간다.

자신을 둘러싸고 있던 모든 것이 산산이 부서지는 소리와 함께, 동천마군은 시야를 물들이며 쏟아지는 백색 화염을 향해 일권을 내질렀다.

후웅!

소리보다 앞선 움직임.

죽은 자와 산 자의 격돌.

새하얗게 물든 세상 속, 느릿하게 나아간 멸염신권(滅炎神拳)이 동천마군의 주먹과 맞닿았다.

아니.

휩쓸었다.

쾅!

한순간의 격돌. 거대한 굉음.

그러나 두 주먹이 서로를 향해 맞닿은 그 시간은 너무나도 짧았고, 힘의 균형은 이미 기울어져 있었다.

콰득.

이미 흐트러져 버린 사기(死氣)를 집어삼킨 열기가 살갗을 짓이긴다. 혈도와 힘줄을 녹이고 뼈마디를 부수었다.

동천마군이 인간으로서의 삶을 포기하며 얻은, 더욱 강건해진 육체와 회복력 따위는 아무런 소용도 없었다.

콰아아아!

적천강의 일권은 용암인 동시에 섬광이었다.

멸염신권이라는 명칭에 담긴 뜻처럼 그가 일으킨 화염은 모든 것을 잿더미로 멸하며 쏘아졌다.

동천마군의 주먹으로도 모자라 그의 한쪽 팔 전체를 집어삼켰다.

화륵, 퍼어엉!

고점에 다다른 화염이 폭발한다.

하지만 마땅히 터져 나와야 할 피도, 그 흔한 살점과 뼛조각조차 찾아볼 수 없었다.

모조리 증발하거나 잿더미가 되어 버렸으니까. 시간을 되돌리지 않는 한 두 번 다시 회복시킬 수 없게 사라져 버렸으니까.

동천마군은 누구보다 그 사실을 잘 알고 있었고, 그것은 적천강 역시 마찬가지였다.

팟.

단 한 걸음.

적천강이 내디딘 발걸음을 따라 공간이 접혔다.

잘못 쏘아진 포탄처럼 뒤로 튕겨 나가던 동천마군이 이를 악물며 신형을 비틀었다.

콰득, 쾅!

옆구리를 스친, 정확히는 스친 것만으로도 한 뼘이나 되는 살점과 뼈를 가루로 만들어 버린 일권이 지면을 강타했다.

동시에 하늘이 쪼개지는 듯한 굉음과 함께 거대한 구덩이가 패었다.

오싹.

동천마군은 전신의 솜털이 곤두서는 듯한 감각을 느꼈다.

과연 자신이 평범한 인간처럼 통증을 느꼈다면, 그렇게 지금의 적천강과 맞섰다면 과연 얼마나 버틸 수 있었을까.

도대체 몇 번째 죽음을 맞이했을까.

‘이건.’

스스로 불사의 존재라고 여겼다. 이미 오래전 사라져 버린 무신이 아닌 이상, 그 누가 온다 해도 쓰러트릴 자신이 있었다.

하지만 아니었다.

‘피하지 못하면, 죽는다.’

동천마군은 살고 싶었다.

이미 한 번 죽은 몸이라 해도 이 삶을 이어 가고 싶었다.

적어도 증오스러운 피를 이어받은 황실과, 태조의 업적이자 유산인 이 대국을 허물어트려야 했다.

복수가 끝날 때까지, 그는 쓰러질 수 없었다.

처참한 죽음을 맞이한 가족과 사문의 사람들.

그리고 이날만을 위해 괴물이 되기를 선택한 동천마군 자신을 위해서라도.

‘난. 나는…….’

으득.

동천마군은 이를 악물었다. 더는 남아 있지 않은 핏물 대신 살점이 떨어져 나갔다.

‘결코 쓰러질 수 없다.’

동천마군 스스로도 알 수 없었다.

그것이 지금까지 이어진 분노인지. 복수에 대한 집념인지.

아니면 일생일대의 대적(大敵)을 맞닥트린 무인이 발휘한 마지막 투혼인지.

다만 한 가지는 확실했다.

앞서 적천강이 그러했듯이 동천마군 역시 기존의 한계를 넘어섰다는 것.

슈확!

찰나의 순간. 벼락처럼 공간을 가로지른 지풍(指風)이 적천강의 목을 관통했다.

아니, 관통한 것처럼 보였다.

연신 물러서는 동천마군을 향해 한 줄기 불꽃이 되어 들이닥치던 적천강의 신형이, 관통당한 목에서 피를 흩뿌리며 쓰러져야 할 그의 모습이 아지랑이처럼 흐트러지기 전까지는.

“……!”

이형환위(移形換位).

그 네 글자가 섬광이 되어 뇌리를 스친 순간, 동천마군은 뒤로 돌아섬과 동시에 하나밖에 남지 않은 팔에 들린 요령을 휘둘렀다.

후웅!

세찬 파공성과 함께 내리그어지는 요령이 사기를 머금고 빛난다.

단 일격. 일격이라도 제대로 적중시킨다면 그 누구라 해도 온전할 수 없다.

그것이 초인이라 불리는 초절정 고수들의 싸움이니까.

화왕과 동천마군. 초절정이라는 세 글자로도 그 무위를 온전히 표현할 수 없는 괴물들의 싸움이니까.

하지만.

콰득.

적어도 지금 이 순간, 어쩌면 오늘 이후로 두 번 다시 도달하지 못할 새로운 경지를 맛보고 있는 누군가에게는 아니었다.

‘고작 이 정도였더냐.’

그건 소리 내어 전해진 육성도, 전음도 아니었다.

그러나 동천마군은 똑똑히 들었다. 보았다.

화염이 깃든 손으로 요령을 붙잡은 채 자신을 응시하는 적천강의 안광에서, 차갑게 다물린 그의 입가에서 들리지 않는 목소리를.

동시에 다음 순간 불길에 휩싸이는 자신의 팔을.

화륵, 콰아아!

산기슭에 번진 화마(火魔)는 며칠이 지나도 사라지지 않지만, 주인의 의지를 따라 일어난 열양지기는 아니었다.

끔찍한 열기를 머금은 그것은 찰나에 시작되어 순식간에 사그라졌다.

하나밖에 남지 않았던, 동천마군의 마지막 팔을 흔적도 없이 녹여 버리며.

하지만 분노한 스승의 응징은 그것으로 끝난 것이 아니었다.

콰직!

동천마군의 시야가 흔들렸다.

팔이 흔적도 없이 녹아내림과 동시에 옆구리를 후려친 일권이, 살과 뼈마디를 부수는 것으로도 모자라 오래전 썩어 버린 그의 오장육부로 화염을 쏟아붓는 것이 느껴졌다.

‘안 돼!’

적천강의 일격, 일격을 허용할 때마다 죽음 역시 한 걸음씩 가까워지는 상황.

쐐애애액!

앞서의 공격으로 상반신의 절반이 새카맣게 그을린 동천마군은 튕겨 나가는 힘을 거스르지 않았다.

오히려 아직 성한 두 다리에 남아 있는 모든 기운을 쏟아부었다.

이미 두 팔과 요령도 잃었다.

최대한 거리를 벌려야 했다.

그리고 온 힘을 다해 땅을 박차며 나아가는 그의 발목을 잡아채는, 만근거력(萬斤巨力)을 느꼈다.

콰직.

살을 짓이기고 뼈를 부수는 힘.

그와 동시에.

후우우웅!

세상이 뒤집혔다. 뭉개지는 바람 사이로 코앞까지 들이닥친 지면이 그를 반겼다.

콰아아앙!

귓가를 먹먹하게 물들이는 굉음과 함께 땅거죽이 솟아오른다.

이미 화강암 지대처럼 딱딱하게 굳어 버린 그곳에, 흙과 바위를 부수며 깊숙이 처박힌 동천마군의 눈꺼풀이 파르르 떨렸다.

‘이건…….’

장장 반백 년을 훌쩍 넘어서는 긴 세월.

황궁에서 암약하며 수많은 초절정 고수를 보았다.

그렇기에 알 수 있었다.

이건 속도와 힘, 어느 것 하나의 문제가 아니라는 것을.

그저 지금의 적천강은, 자신보다 앞선 영역에 있다는 것을.

콰드드득!

단 한 줌의 통증조차 없다. 그래서 더욱 선명하게 느껴진다.

그에게 남아 있던 두 다리 중 하나가 지금 막 뽑혀 나갔음을.

그리고 그 사실은 곧 한 가지를 의미했다.

‘이제는…… 더 물러날 곳도 없군.’

동천마군은 실소를 흘렸다.

비로소 코앞에 닥친 죽음을 받아들인 자의 미소?

아니었다.

오랜 세월 기다린 복수와 목숨 중 한 가지를 선택할 수밖에 없었던, 결국 최후의 순간에 뽑아 들고자 숨겨 두었던 복검(覆劍)을 드러내기로 결심한 자의 씁쓸한 웃음이었다.

― 나오게, 천살(天殺).

그리고 의미를 알 수 없는, 희미한 한 줄기의 전음이 달싹이는 입술 사이로 흘러나온 그 순간.

스륵.

텅 빈 허공이 일렁였다.

흩날리는 잿더미와 불씨 사이로 떨어져 내린 살수(殺手)가, 절름발이라는 것이 무색하리만치 섬광처럼 쏘아진 노인이 적천강의 정수리 위로 비수를 내리그었다.

솨악!

완벽에 가까운. 아니, 누구도 부정할 수 없는 완벽한 암습이 성공하려던 그때.

쐐애애애액!

한 자루의 창이, 한 줄기의 화염이 되어 공간을 갈랐다.
```

## Final English reading copy

```markdown
# Chapter 917

*Fwoosh.*

A fierce gale roared through the air. Layers of black ash that had piled up across the ground, along with embers that still hadn’t gone out, rode the wind and scattered in every direction.

Then, from within that pale haze that blocked everyone’s view, a fist wreathed in flames cleaved through space.

*BOOM! KABOOOOOM!*

Compressed air burst apart. Beyond the scorching air, white flames surged.

It was a fire nothing could stop.

The breath of a dragon. Its roar. A rage so vast it could not be measured.

The flames of the old dragon poured down on those who had dared touch his reverse scale, burning more fiercely than ever.

So fiercely that someone who had already become nearly immortal found himself thinking of the word *death* without even realizing it.

*Ah.*

The Eastern Heaven Demon Lord let out a quiet groan.

His gray eyes, now a mix of fear and awe, remained fixed on the man approaching him, endlessly pouring out flames.

Jeok Cheongang, the Fire King.

It was him.

Only him.

The ten Kings who had failed to reach that lofty heaven.

And now, the foremost among them—the Emperor of Fire—was finally spreading the wings he had kept hidden and soaring upward.

Toward the three stars adorning the heaven called the Martial God.

Pouring out his rage at the enemies who had touched what they should never have touched.

*Rumble.*

A tremendous impact hammered his entire body.

The death energy that had surrounded the Eastern Heaven Demon Lord without a gap shuddered beneath a palm strike imbued with unprecedented power.

His legs, planted in the ground with roughly six tons of force, carved deep furrows as they were driven backward.

*BAM! BAM! KABOOM!*

One advanced.

The other had no choice but to retreat.

Jeok Cheongang was the former; the Eastern Heaven Demon Lord, the latter.

He was like a sinner hunched low, desperately dodging the thunderbolts raining down without pause like divine punishment.

*How? How in the world…?*

How could that exhausted body, already covered in wounds great and small, wield such strength?

How could he feel such rage?

The Eastern Heaven Demon Lord swallowed the sigh that rose to his lips.

And found himself understanding the fierce anger of Jeok Cheongang, approaching with an overwhelming aura—his rage so intense it felt as if he could reach out and touch it.

Because he was the same.

*BAM!*

He had lost his family.

*BAM!*

He had lost his sect.

*BAM!*

When he thought he had lost everything, he found something left in a corner of his emptied heart.

*Rage.*

They said a person was human because they could feel joy, anger, sorrow, and pleasure.

They said a being was alive because it could laugh, rage, grieve, and feel joy.

But the Eastern Heaven Demon Lord had lost three of those things.

With nothing left but rage, he had finally given up on being human and become a monster.

A monster called a vengeful spirit.

That was why, in a way, he understood Jeok Cheongang—the feelings of an old Master who had seen his Disciple standing at the crossroads between life and death.

He understood, too, the rage held within that mighty flame, which was trying to burn even the death energy he had summoned with all his might.

*KABOOOOOM!*

In that instant,

the Eastern Heaven Demon Lord felt it.

The death energy encircling him had finally reached its limit.

At this moment, Jeok Cheongang’s rage had surpassed his own.

*Crack.*

The sound announcing a rift reached the Eastern Heaven Demon Lord’s ears. The energy that had poured ceaselessly from deep within his body was scattering.

At the starting point of that rift was a fist wreathed in pure white flames—and a pair of eyes pouring out stream after stream of fire and an even greater heat, flames that would bring down his last line of defense.

“Understand this clearly.”

The light in Jeok Cheongang’s eyes seemed capable of turning anything it faced to ash.

“Understand what you’ve touched.”

Yet his voice was as cold as the glaciers of the North Sea. It froze the Eastern Heaven Demon Lord’s spine and seeped into his soul.

It awakened a fear he had long forgotten, ever since the day he rose from death.

*Hah.*

The Eastern Heaven Demon Lord trembled without meaning to. A hollow laugh escaped him.

And suddenly, he understood.

*Perhaps the Three Saints… or even beyond.*

At least at this moment, there was nothing that could stop the old dragon’s rage.

Nothing.

*CRASH!*

At last, it split and shattered.

As everything surrounding him broke to pieces, the Eastern Heaven Demon Lord thrust out his fist toward the white flames flooding his vision.

*Whoosh!*

A movement faster than sound.

The dead clashed with the living.

In a world turned pure white, the Flame-Extinguishing Divine Fist advanced slowly and met the Eastern Heaven Demon Lord’s fist.

No.

It swept right through it.

*BAM!*

The clash lasted only an instant. A tremendous boom rang out.

But the time their fists met was far too brief, and the balance of power had already tipped.

*Crack.*

Heat swallowed the scattered death energy and crushed his skin. It melted his acupoints and sinews, then shattered his bones.

The stronger body and resilience the Eastern Heaven Demon Lord had gained by abandoning his life as a human were of no use.

*KABOOOOOM!*

Jeok Cheongang’s fist was lava and lightning at once.

As its name implied, the flames he unleashed—the Flame-Extinguishing Divine Fist—shot forward, reducing everything to ash.

They swallowed not only the Eastern Heaven Demon Lord’s fist, but his entire arm.

*Fwoosh. BOOM!*

The flames erupted at their peak.

But there was no blood, no scraps of flesh, not even the common fragments of bone that ought to have burst from the wound.

They had all vaporized or turned to ash. They had vanished beyond any hope of recovery unless time itself could be turned back.

The Eastern Heaven Demon Lord knew that better than anyone.

So did Jeok Cheongang.

*Step.*

With a single stride, Jeok Cheongang folded the space before him.

The Eastern Heaven Demon Lord, thrown backward like a misfired cannonball, gritted his teeth and twisted around.

*Crack. BAM!*

The fist that grazed his side—though “grazed” meant it had pulverized a chunk of flesh and bone a handspan wide—slammed into the ground.

At the same time, a tremendous boom split the sky, and a massive crater opened in the earth.

A chill ran through him.

The Eastern Heaven Demon Lord felt as though the hairs all over his body were standing on end.

If he could feel pain like an ordinary human, if he had fought Jeok Cheongang as he was now, how long would he have lasted?

How many times would he have died?

*This is…*

He had thought himself immortal. Unless the Martial God, who had vanished long ago, returned, he had been confident no one who came for him could bring him down.

But that wasn’t true.

*If I can’t dodge, I’ll die.*

The Eastern Heaven Demon Lord wanted to live.

Even if he had already died once, he wanted to keep living this life.

At the very least, he had to bring down the Imperial House, heir to that loathsome bloodline, and this Great Nation, Taizu’s achievement and legacy.

Until his revenge was complete, he could not fall.

For his family and fellow members of his sect, who had met such horrific deaths.

And for himself—the Eastern Heaven Demon Lord, who had chosen to become a monster for the sake of this very day.

*I. I…*

*Grind.*

The Eastern Heaven Demon Lord clenched his teeth. With no blood left, pieces of flesh fell away instead.

*I cannot fall. Not ever.*

Even the Eastern Heaven Demon Lord himself couldn’t tell what it was.

Was it the rage that had carried him this far? His obsession with revenge?

Or the last fighting spirit of a martial artist who had finally met the greatest enemy of his life?

One thing was certain.

Just as Jeok Cheongang had moments earlier, the Eastern Heaven Demon Lord had also surpassed his former limits.

*Whoosh!*

In the blink of an eye, Finger Qi streaked across space like lightning and pierced Jeok Cheongang’s neck.

No—it only looked as though it had pierced him.

The Jeok Cheongang who had charged at the retreating Eastern Heaven Demon Lord like a streak of flame—whose image should have fallen with blood spraying from its pierced neck—did not unravel like a heat haze until then.

“……!”

At the instant those four characters flashed through the Eastern Heaven Demon Lord’s mind—Shifting Form and Position—he spun around and swung the bell clutched in his only remaining arm.

*Whoosh!*

The bell sliced down with a fierce whistle, gleaming as it brimmed with death energy.

A single blow. If even one strike landed cleanly, no one could come away unscathed.

That was the nature of battles between the Supreme Peak masters called superhuman.

The Fire King and the Eastern Heaven Demon Lord—monsters whose martial prowess could not be fully expressed even by the three words “Supreme Peak.”

But—

*Crack.*

Not against someone who, at least in this moment, had reached a new realm—one he might never reach again, perhaps not even after today.

*Was that all you had?*

It wasn’t a voice spoken aloud, nor was it Sound Transmission.

But the Eastern Heaven Demon Lord heard it clearly. He saw it, too.

In the fire-wreathed hand that gripped the bell and the fiery gaze that fixed on him; in Jeok Cheongang’s tightly closed lips, he heard a voice that made no sound.

At the same time, he saw his own arm engulfed in flames in the next instant.

*Fwoosh! KABOOOOOM!*

A fire that spread over a mountainside might burn for days before it died out. But the Scorching Yang Qi that rose at its master’s Will did not.

It carried a dreadful heat, but it began in an instant and faded just as quickly.

It melted the Eastern Heaven Demon Lord’s only remaining arm without leaving a trace.

But the punishment of the enraged Master did not end there.

*CRACK!*

The Eastern Heaven Demon Lord’s vision shook.

As his arm melted away without a trace, a fist smashed into his side. It crushed flesh and bone, then poured flames into his long-rotted internal organs.

*No!*

Every blow from Jeok Cheongang brought death one step closer.

*SHWAAAA!*

Half the Eastern Heaven Demon Lord’s upper body had been scorched black by the previous attack. He didn’t resist the force throwing him backward.

Instead, he poured all the energy left in his still-healthy legs into his escape.

He had already lost both arms and the bell.

He had to put as much distance between them as possible.

But as he kicked off the ground with all his strength, he felt a force of roughly six tons seize his ankle.

*Crack.*

A force that crushed flesh and shattered bone.

And at the same time—

*Whoooosh!*

The world turned upside down. Through the crushing wind, the ground rushed up to meet him.

*KABOOOOOM!*

A thunderous roar drowned out his ears, and the earth’s crust surged upward.

His eyelids trembled as he lay buried deep in the ground, breaking through dirt and rock in a place that had hardened as solid as granite.

*This is…*

For well over half a century, he had operated in the shadows of the Imperial Palace and observed countless Supreme Peak masters.

That was why he knew.

This wasn’t a matter of speed or strength.

It was simply that Jeok Cheongang now stood in a realm beyond his.

*Rumble.*

He couldn’t feel even a shred of pain. That was why he felt it all the more clearly.

One of the two legs he had left had just been torn off.

And that meant one thing.

*There’s nowhere left to retreat.*

The Eastern Heaven Demon Lord let out a hollow laugh.

Was it the smile of someone who had finally accepted the death bearing down on him?

No.

It was the bitter laugh of someone who had waited so long for revenge, but had been forced to choose between that and his life—and who had decided to reveal the hidden sword he had meant to draw at the very end.

“—Come out, Heaven’s Slaughter.”

And just as a faint line of Sound Transmission, its meaning unclear, slipped between his moving lips—

*Shiver.*

The empty air wavered.

An assassin dropped through the drifting ash and embers. An old man shot forward like a flash of light, his limp belying his speed, and slashed a dagger down at the crown of Jeok Cheongang’s head.

*Whoosh!*

An ambush close to perfect—no, a perfect ambush that no one could deny—was about to succeed when—

*SHWAAAA!*

A spear, a streak of flame, cut through space.
```
