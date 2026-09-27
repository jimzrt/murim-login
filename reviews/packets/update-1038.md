<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1038.txt",
      "sha256": "567fb1d3281aa0faca6bc287b4bdf5ac7bf71530b4d283cd2c2c6f4ef6f01e3a",
      "bytes": 13774
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1ba5c3c29ae65f58707fe993363d720383fb60fa669eb9b3d56bde5d15744847",
      "bytes": 1496
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "383045aaa550afcd5ef9913b67eee36e7dfcbd478f5edeb7be10bfbb7930e01e",
      "bytes": 240741
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "f7342a79c28887f5950363ee1cc46edac9ad06ed4908ea97d2f12d91812145af",
      "bytes": 914
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "008398b5e1b13687d4e015b8935550a7e3b99d330e5498d3217fcf6d2800b7b5",
      "bytes": 1502
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ffda7b1b005b577c9f645bf02ac2b230caa0b62d834a92d96bd2e9c401c9640b",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f78099b144ce0321743eec5fdf0c165083ec3e8ae3c8bf959eafb1b530843846",
      "bytes": 279561
    }
  ],
  "estimated_tokens": 9956
}
-->

# Durable State Update — Chapter 1038

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
1 and safe_through 1038. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1038. Profile updates may replace only one
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
  "chapter": 1038,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1038,
    "continuity_sources": [1038],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang and Jin Taekyung are fighting on the battlefield; Jeok is wounded and facing the Blood-Sword Demon Lord.",
    "Sama Pyo stayed in the front line rather than dodge an attack into an ally; a young Black Dragon Demon Gate martial artist died saving him.",
    "Sima Gong arrived at the front with the Black Dragon Demon Gate’s elite after delaying his intervention; he had ordered two men placed in the front line, and both died.",
    "Sama Pyo openly challenged Sima Gong and chose a path different from his father’s; he says the Black Dragon Demon Gate will survive regardless of the battle’s outcome.",
    "Jin Taekyung controls many weapons with his Will, but they are depleted or deflected as he advances through the enemy ranks.",
    "Jin Taekyung launched White Flame at the Blood-Sword Demon Lord; the result is unresolved."
  ],
  "continuity_sources": [
    1036,
    1037
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what is the white-robed followers’ purpose?",
    "How do the white-robed followers’ Magic and the Wind Ghost’s power work?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1037,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 일격     | **One Strike**                         |
| 레벨               | **Level**                      |
| 마법사     | **mage**              |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이기어검 | **Qi-Controlled Sword** | Technique used by the Western Heaven Demon Lord to control and attack with a sword through qi. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 황하 | **Yellow River** | River along which civilization began. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 척방혈 | **Chuk Banghyeol** | The Blood-Sword Demon Lord’s name, revealed by Taekyung’s Qi Sense. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1037
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1037
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1036
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1038화



아마도 한계 이상으로 끌어 올린 중단전의 이능(異能) 때문일 것이다.

저벅.

죽은 것과 산 것.

그 모든 것이 증발하고 오직 붉게 물든 혈로(血路)에 걸음을 내디딘 그 순간, 지금껏 느껴 본 적 없던 극심한 두통이 엄습해 오는 것은.

‘흡.’

마치 길고 예리한 바늘이 머릿속을 들쑤시는 듯한 격통.

그러나 나는 온 힘을 다해 신음을 참고 파르르 떨리는 신형을 애써 억제했다.

이미 날카로운 이빨을 드러낸 맹수의 앞에서 조금이라도 약한 모습을 보였다간 그 즉시 잡아먹히고 말 테니까.

“그래, 왔느냐?”

혈검마군(血劍魔君).

태연하기 그지없는 놈의 목소리를 듣는 순간, 두통이 배가 되어 부풀어 오른다.

아니, 어쩌면 진짜 이유는 어느덧 피투성이가 되어 버린 적천강의 모습 때문일지도 모른다.

혹은.



[Lv.??? 척방혈]



이제는 현재의 내 수준으로도 정확히 측정할 수 없는 진정한 괴물로 거듭난 혈검마군의 강함을 확인했기 때문일지도.

‘최소 20레벨 차이……. 더 힘든 싸움이 되겠군.’

마음속으로 신음을 삼키며 손을 뻗자 보이지 않는 선으로 이어진 백염이 쏜살같이 되돌아와 손아귀에 잡혔다.

내심 경계하고 있던 나 스스로가 무색해질 만큼, 아무런 방해조차 없이.

“이기어검. 아니, 이기어창(以氣馭槍)이라고 해야 하나? 어지간히 급했나 보군. 이렇게까지 무리할 정도라면.”

여유로운 태도와 음성.

한 수 위의 강자만이 보일 수 있는 모습으로, 혈검마군은 사람 좋은 미소를 만면에 띄웠다.

“그래도 칭찬해 주지. 좋은 시도였어. 최소한 스승이 죽기 전에는 돌아왔으니.”

그리고 혈검마군이 웃으며 슬쩍 손을 흔든 그 순간, 빈틈을 발견한 적천강이 벼락처럼 손을 뻗었다.

“놈!”

콰아아아!

대갈일성과 함께 뻗어 나가는 열기.

그러나 모든 것을 불사르며 나아가는 화염신장(火焰神掌)의 장력이 면전까지 들이닥친 그 순간에도 혈검마군의 입가에 맺힌 미소는 여전했다.

다만 유일하게 달라진 것이 있다면 어느새 공간을 가로지르고 있는 한 줄기의 핏빛 검강(劍罡)이었다.

슈확! 꽈아아앙!

정확히 반으로 갈라진 장력이 좌우로 튕겨 나가 지면을 후려친다.

반경 십여 장을 집어삼킨 굉음과 매캐한 연기 속, 마치 유령처럼 홀연히 모습을 드러낸 혈검마군이 검을 내리그었다.

쏴아아악!

끔찍하리만치 막강한 압력에 의해 일그러지는 공간.

하지만 태산도 베어 낼 듯한 그 검격을, 적천강은 이미 예상하고 있었다는 듯이 옆으로 몸을 날렸다.

서걱!

마치 두부처럼 갈라지는 지면.

그 치명적인 위력이 담긴 일격을 아슬아슬하게 피해 낸 적천강은 곧바로 몸의 중심을 바로 세웠지만, 흐릿해진 혈검마군의 신형은 이미 그의 측면을 향해 나아가고 있었다.

‘위험……!’

나조차도 뒤늦게 반응할 수밖에 없었던 속도.

소리 내어 외칠 틈조차도 없었다.

불과 호흡 한번 내뱉을 정도로 되지 않는 그 짧은 시간 동안 두 초인은 섬광처럼 공방을 주고받았고, 혈검마군의 움직임은 소리조차 앞질러 나아가고 있었으니까.

후우웅, 퍼엉!

압축된 공기가 터져 나간다.

검을 휘두르기에는 너무나도 좁혀진 거리.

혈검마군이 뻗은 일장에 어깨를 격중당한 적천강의 신형이 포탄처럼 뒤로 튕겨 나갔다.

그리고 그 방향의 끝에는.

쐐애애액, 턱!

온 힘을 다하여 적천강을 돕기 위해 달려가던 내가 있었다.

“노야!”

나도 모르게 터져 나온 다급한 외침.

빠르게 튕겨 나가던 와중, 내 도움으로 간신히 멈출 수 있게 된 적천강이 쇳소리가 섞인 음성으로 대꾸했다.

“노부는 아무렇지도 않으니 괜히 호들갑 떨지 말고 목소리나 줄여라. 귀청 떨어지겠구먼.”

다른 사람이라면 별다른 차이를 못 느낄 만큼 평소와 다름없이 퉁명스러운 어조였지만, 화왕 적천강에 대해 세상 그 누구보다 잘 알고 있는 나는 아니었다.

그는 위험할수록 태연을 가장한다.

다른 누군가를 안심시키기 위해서라도.

“또 이러시네. 약 드실 시간입니다.”

한숨을 내쉰 나는 적천강의 등에 손을 대고 망설임 없이 공력을 흘려보냈다.

툭. 스아아아.

본디 불과 불은 한 몸이라.

한 뿌리에서 비롯된 열양지기는 그렇게 순식간에 서로를 향해 이어졌고, 몸 안 깊숙이 고여 있던 노폐물들을 몰아냈다.

“쿨럭.”

투두둑.

주인의 의지와는 다르게 입술 사이로 울컥 흘러넘치는 한 움큼의 핏물.

적지 않은 내상을 의미하듯, 시커멓게 물든 그것을 확인한 나는 작게 혀를 찼다.

“아무렇지도 않다고요?”

퉤, 하고 피가래를 뱉은 적천강이 대꾸했다.

“그깟 피 한 모금 뱉었다고 수선은.”

솔직히 이런 상황에서는 그냥 넘어가고 싶지만, 사실 여부 확인이라는 절차는 아주 중요하다.

목숨이 걸려 있다면 더더욱.

뻐억!

조금 전의 일격으로 많이 줄어들긴 했으나, 그래도 아직 후방에 남아 있던 적의 병력은 상당수.

그새를 못 참고 달려들던 적의 가슴을 걷어차 함몰시키며, 나는 적천강에게 물었다.

“이미 전신이 피범벅이신 건 아시고 하신 말씀이죠?”

“노부가 흘린 거 아니다. 이리저리 바쁘게 움직이다 보니 어쩌다가 묻은 거지.”

“저쪽은 아주 멀쩡한데요.”

갈라지는 인의 파도 속, 느긋하게 걸음을 옮겨 다가오는 혈검마군을 가리키자 적천강이 작게 입맛을 다셨다.

“덜 바빴나 보지.”

“아하. 덜 바빴다. 그렇군요.”

“여하튼 노부는 멀쩡하다. 생채기 하나 없……진 않지만, 이 정도로는 끄떡도 없어.”

퍼엉!

신형을 일으켜 세우는 동시에 세 명의 적을 숯덩이로 만들어 버린 적천강이 입가에 묻은 핏물을 핥았다.

“어떠냐.”

“그냥 솔직히 말씀하십쇼. 다른 사람들한테는 비밀로 할 테니까.”

“이런 천인공노할 놈 보게. 지금 노부가 허풍이라도 떨고 있다는 말이냐?”

“아닙니까?”

“아니다. 저깟 놈이 뭐라고.”

“그럼 저는 가 보겠습니다.”

“응?”

“저깟 놈은 혼자서도 충분하실 거 아닙니까. 다른 사람들은 지금도 죽을 맛이에요.”

덥석.

슬쩍 몸을 돌리기 무섭게 번개처럼 내 손목을 잡아챈 적천강이 준엄한 목소리로 대답했다.

“옛 현인들께서 말씀하시길, 백지장도 맞들면 낫다고 했다.”

“…….”

“무슨 수작을 부렸는지는 몰라도 어느 순간마다 놀라울 정도로 강해지고, 빨라지더군. 귀신에 홀린 게 아닌가 싶을 정도로.”

“…….”

“그뿐만인 줄 아느냐? 노부가 전력을 다해 공격을 격중시키려 할 때마다 알 수 없는 힘이 막, 막…….”

“노야.”

장황하게 이어지려는 말을 끊어 낸 내가 나직하게 덧붙였다.

“혓바닥이 너무 기십니다.”

“…….”

“한 줄 요약하시죠. 간단명료하게.”

잠시 침묵하던 적천강이 대답했다.

내가 앞서 요청했던 대로, 아주 간단명료하게.

“저 새끼 존나 쎄.”

“완벽한 표현이네요.”

“그리고 저 멀리 뒤에 있는 새하얀 것들이 괴이하기 짝이 없는 사술(邪術)로 놈을 돕고 있다. 한 번씩 특유의 이상한 기운이 요동칠 때마다 놈이 강해지더군. 하여 더 상황이 악화되기 전에 무리해서라도 저놈들부터 처리하려 했지만…….”

“실패하셨겠죠. 노야 역시 그 사술에 당해서.”

“그래, 맞다. 그때 노부가 느낀 감각은 마치…….”

“하늘이 짓누르는 것 같았고요.”

중력 마법이다. 틀림없는.

그리고 더할 것도 뺄 것도 없는 정확한 표현에 문득 멍해진 적천강을 향해, 나는 담담한 어조로 말을 이었다.

“정확히 말씀드리자면, 저건 일반적인 사술이 아닙니다. 마법이라고 부르는 능력이죠.”

“잠깐, 마법이라면.”

“예. 노야께서도 아시는 바로 그 마법입니다. 제 고향에서나 볼 수 있었던.”

“……!”

그 순간, 적천강이 눈을 부릅뜬 것은 당연한 반응이었다.

비록 세세한 것 전부는 아니더라도, 그는 내가 어디에서 왔으며 그곳이 어떤 세상인지 어느 정도는 들어서 알고 있었으니까.

하지만 그런 적천강조차 지금 이 상황을 온전히 이해하고 받아들일 수는 없었다.

그건 나 자신조차 불가능한 일이었으니.

다만 이러한 사실들보다도 중요한 것은, 눈앞의 적을 쓰러트려야 한다는 점이다.

- 놈들을 먼저 노려야 합니다. 혈검마군이 아니라 저 새하얀 옷을 입은 자들……. 아니, 마법사들을요.

전음을 흘려보내면서도 등골이 서늘해질 만큼 낯설었다.

마법사. 마법사라니.

그것도 현대가 아닌 바로 이곳, 무림에서.

하지만 지금 이 순간에도 산보하듯 여유로운 발걸음으로 거리를 좁혀 오는 혈검마군의 어깨 넘어, 언덕 위에서 백색 옷자락을 휘날리는 마법사들의 모습을 보자 직면하고 있는 현실이 피부에 와닿았다.

‘무슨 수를 써서라도 저놈들부터 제거해야 한다.’

마법사의 존재를 처음으로 인지했을 때부터 그 외의 선택지는 내 머릿속에 없었다.

나는 이미 알고 있다.

지금 이 전장에 선, 혹은 쓰러지고 있는 수만 명의 아군 중 오직 나만이 알고 있었다.

마법이라는 단어에 어느 정도의 변수와 위험이 도사리고 있는지.

또한 그 놀라운 이능을 허락받은 마법사들이 이 같은 대규모 전투에서 어느 정도의 위력을 발휘할 수 있는지.

게다가…….

‘저들 중 유독 뛰어난 마법사가 있다. 그것도 나와 노야를 마법으로 저지할 정도의 실력을 지닌.’

작동 원리가 다를 뿐, 결국 마법 역시도 기(氣)라는 원료를 바탕으로 발현되는 것.

그렇기에 나나 적천강에게 있어, 제법 높은 경지에 오른 마법사라 해도 별다른 위협이 되지는 못한다.

진리의 끝자락에 다다랐다고 표현되는 극소수의 존재들을 제외한다면.

“……대마도사(大魔道士).”

나도 모르게 신음처럼 입술을 비집고 흘러나온 네 글자.

그리고 대마도사의 존재를 확신하려던 그 순간, 불현듯 뇌리에 떠오른 한 가지 의문.

‘정말 놈들 중에 대마도사가 있다면, 어떻게 지금 같은 상황이 유지되고 있는 거지?’

우리가 유리하다는 뜻이 아니다.

비록 나를 포함한 모두가 최선을 다하고 있다 해도, 현재로서는 아군에게 있어 전황이 어렵게 흘러가고 있는 것이 사실이었으니까.

‘하지만 대마도사가 나섰다면, 이 불리한 전황을 유지하고 있는 것조차도 어려웠겠지.’

대마도사가 전장에 끼치는 영향을 누구보다 잘 알고 있는 나로서는, 길게 생각해 볼 것도 없는 일이었다.

지금껏 천하의 그 누구도 본 적 없던 광범위 공격 마법.

의지를 지닌 자연재해와도 같은 불가해(不可解)의 능력 앞에서, 삼분지 일 이상이 오합지졸로 이루어진 아군이 얼마나 버틸 수 있겠나.

그러나 예의 대마도사는 나서지 않았다.

중력 마법으로 나와 적천강을 일시적으로 방해하고, 신체 강화 마법으로 혈검마군을 도왔을지언정 그 이상은 개입하지 않고 있었다.

철벅.

피로 붉게 물든 길을 가로지른 혈검마군의 발걸음이, 마침내 우뚝 멈춰선 지금 이 순간에도.

“도대체…… 뭘 노리고 있는 거지?”

진심으로 궁금했고, 동시에 불안했다.

마법사들이 별다른 조치를 취하지 않는 이유가 단번에 이 전투를 끝낼 강력한 마법을 준비하고 있기 때문인지.

아니면 또 다른 흉계를 꾸미고 있는 것인지.

그리고 내가 참지 못하고 불쑥 던진 물음에, 삼 장 밖에서 웃는 얼굴로 우리를 응시하고 있던 혈검마군이 문득 미간을 좁혔다.

“노린다니? 내가 이 전투에서 노리는 건 처음부터 두 가지뿐이었어. 승리. 그리고 자네.”

“대답해 주기 싫다는 말을 길게도 하는군.”

“뜬금없이 무슨 소린지 모르겠지만……. 뭐, 상관없지.”

진심인지, 연기인지 알 수 없는 표정으로 어깨를 으쓱한 혈검마군이 느슨하게 늘어트렸던 검을 들어 올리며 말을 이었다.

“이제 끝을 보지. 물론 한 사람은 죽고, 한 사람은 사로잡히는 결말이 좋겠어.”

나와 적천강이 동시에, 한 목소리로 대답했다.

“좆 까.”

그리고 그 순간.

파팟!

우리는 혈검마군을 향해 달려들었다.

아니, 정확히는 적천강만이 놈을 향해 쏘아졌다.

- 반 각. 반 각만 놈을 붙잡아 주십시오.

바람 사이로 흘려보낸 전음과 함께, 신형을 비튼 나는 언덕을 향해 쇄도했다.

쐐애애액!
```

## Final English reading copy

```markdown
# Chapter 1038

It was probably because of the Middle Dantian’s ability, which I’d pushed beyond its limits.

Step.

The dead and the living.

The moment I stepped onto that blood-red path, with everything else evaporated away, an agonizing headache unlike anything I’d ever felt before came crashing down on me.

*Hup.*

A pain like a long, sharp needle probing around inside my skull.

But I gritted my teeth and held back a groan, doing my best to suppress my trembling body with every ounce of strength I had.

If I showed even the slightest weakness in front of a beast that had already bared its fangs, it would devour me on the spot.

“So, you’ve come?”

The Blood-Sword Demon Lord.

The moment I heard his utterly unruffled voice, my headache swelled twice as strong.

No—or maybe the real reason was the sight of Jeok Cheongang, now drenched in blood.

Or perhaps…

> **System**
> **Lv. ???**
> **Chuk Banghyeol**

Maybe it was because I’d confirmed the strength of the Blood-Sword Demon Lord—a true monster who’d grown beyond anything I could accurately measure at my current level.

*At least a twenty-Level gap… This is going to be a much harder fight.*

Swallowing a groan, I reached out. White Flame, still connected to me by an invisible thread, shot back into my grasp.

Without the slightest interference—enough to make all my earlier caution feel foolish.

“Qi-Controlled Sword. No, should I call it Qi-Controlled Spear? You must’ve been in quite a hurry to push yourself this far.”

His relaxed manner and voice.

The Blood-Sword Demon Lord wore the easy smile of a man who knew he was stronger than his opponent.

“Still, I’ll give you credit. It was a good try. At least you made it back before your master died.”

And the instant the Blood-Sword Demon Lord laughed and casually waved his hand, Jeok Cheongang spotted an opening and thrust out his palm like lightning.

“You bastard!”

KWA-AAAH!

A wave of heat surged forward with his shout.

Even as the force of Flame Divine Palm, burning everything in its path, bore down on the Blood-Sword Demon Lord’s face, the smile on his lips didn’t change.

The only thing that did was a streak of blood-red Sword Force, now cutting through the space between them.

SHWAK! KWA-BOOM!

The palm force split precisely in two. The halves ricocheted left and right, slamming into the ground.

A roar swallowed everything within a dozen *jang*, and acrid smoke billowed into the air. Through it, the Blood-Sword Demon Lord appeared like a ghost and swept his sword down.

SHWAAASH!

The space warped under the horrifying pressure.

But Jeok Cheongang seemed to have anticipated the sword strike, powerful enough to cleave a mountain, and threw himself to the side.

SHK!

The ground split like tofu.

Jeok Cheongang narrowly avoided that deadly strike and immediately righted himself. But the Blood-Sword Demon Lord’s fading figure was already darting toward his flank.

*Danger…!*

He was so fast that even I could only react a beat too late.

There wasn’t even time to shout.

In the briefest moment—less than a single breath—the two superhumans exchanged attacks like streaks of light. The Blood-Sword Demon Lord’s movements were faster than sound itself.

WHOOOM—PAM!

Compressed air burst apart.

They were too close to swing a sword.

The Blood-Sword Demon Lord struck Jeok Cheongang in the shoulder with his outstretched palm, sending him flying backward like a cannonball.

And at the end of that flight—

SHWEEEE—THUD!

It was me, racing at full speed to help Jeok Cheongang.

“Old Master!”

The panicked shout burst from me before I knew it.

Jeok Cheongang was hurtling backward, but with my help, he just barely managed to stop himself. His reply came in a rasping voice.

“I’m fine. Stop making a fuss and lower your voice. You’ll burst my eardrums.”

His tone was as gruff as ever, so familiar that most people wouldn’t have noticed a difference. But I knew the Fire King Jeok Cheongang better than anyone in the world.

The more dangerous things got, the more he pretended to be calm.

If only to reassure someone else.

“You’re doing it again. Time for your medicine.”

With a sigh, I placed a hand on Jeok Cheongang’s back and poured internal energy into him without hesitation.

Tap. Fwoosh.

Fire and fire were one and the same.

The Scorching Yang Qi that sprang from the same source joined together in an instant, driving the impurities pooled deep inside his body out of him.

“Cough.”

Drip-drip.

A mouthful of blood welled up between his lips, against his will.

I clicked my tongue when I saw how black it was—a sign of a serious Internal Injury.

“You’re fine, are you?”

Jeok Cheongang spat out a bloody phlegm with a *ptoo*.

“It’s just a mouthful of blood. What’s there to make a fuss about?”

Honestly, I wanted to let it go in a situation like this. But confirming whether someone was telling the truth was important.

All the more so when their life was on the line.

THWACK!

The enemy had lost many in that last attack, but plenty of their forces still remained in the rear. As one of them charged at us before he could hold back, I kicked him in the chest and caved it in.

“Sure, after you’ve already been covered head to toe in blood?”

“I didn’t spill it. I got busy running around, and somehow it got on me.”

“That guy looks perfectly fine.”

I pointed toward the Blood-Sword Demon Lord, who was strolling toward us through the parting waves of men. Jeok Cheongang smacked his lips quietly.

“Then he must’ve been less busy.”

“Ah. Less busy. I see.”

“Anyway, I’m fine. Not a scratch on me… Well, not quite, but this is nothing.”

PAM!

Jeok Cheongang sprang upright and turned three enemies to charcoal in the same motion. Then he licked the blood from the corner of his mouth.

“Well?”

“Just tell me the truth. I won’t tell the others.”

“You insolent brat. Are you saying this old man is making things up?”

“Are you not?”

“I’m not. What does a bastard like him amount to?”

“Then I’ll go help the others.”

“Hm?”

“You can handle a bastard like him by yourself, right? Everyone else is having the worst time of their lives out there.”

GRAB!

The instant I started to turn away, Jeok Cheongang snatched my wrist like lightning and replied in a stern voice.

“The wise men of old said, ‘Even a sheet of paper is easier to lift when two people carry it.’”

“……”

“I don’t know what trick he’s using, but every so often he gets shockingly stronger and faster. It’s almost as if he’s possessed by a ghost.”

“……”

“And that’s not all. Whenever this old man tried to hit him with all my strength, some unknown force kept stopping me, stopping—”

“Old Master.”

I cut off the long-winded explanation and added quietly,

“You’re talking too much.”

“……”

“Sum it up in one sentence. Keep it short and clear.”

Jeok Cheongang fell silent for a moment, then answered.

Just as I’d asked: short and clear.

“That bastard’s strong as fuck.”

“Perfectly put.”

“And those pure-white things way over there are helping him with some bizarre dark arts. Every time that strange energy of theirs surges, he gets stronger. I tried to take them out before things got even worse, even if I had to overextend myself, but…”

“You failed. You got hit by those dark arts, too.”

“Right. The sensation I felt then was like…”

“Like the sky was crushing you.”

Gravity magic. No doubt about it.

Jeok Cheongang looked momentarily stunned by how exact—and no more than exact—my description was. I continued in a calm voice.

“More precisely, that’s not ordinary dark arts. It’s an ability called Magic.”

“Wait. If you mean Magic…”

“Yes. The very Magic you know. The kind you’d only see in my homeland.”

“……!”

Jeok Cheongang’s eyes widening was only natural.

Though I hadn’t told him every last detail, he knew a little about where I came from and what kind of world it was.

But even Jeok Cheongang couldn’t fully understand or accept what was happening now.

Neither could I.

Still, more important than any of that was the fact that we had to defeat the enemy in front of us.

*We have to target them first. Not the Blood-Sword Demon Lord, but those white-robed people… the mages.*

Even as I sent him the message through Sound Transmission, a chill ran down my spine at how unfamiliar the idea felt.

Mages. Mages.

And here they were—not in the modern world, but right here in the Murim.

But when I saw the mages in their white robes fluttering on the hill behind the Blood-Sword Demon Lord, who was still narrowing the distance between us at a leisurely stroll, the reality I was facing finally sank in.

*We have to take them out first, no matter what.*

From the moment I’d first realized the mages existed, there had been no other option in my mind.

I already knew.

Of the tens of thousands of allies on this battlefield—standing their ground or already falling—I was the only one who knew.

How many variables and dangers lurked behind the word *Magic*.

And how much power mages blessed with that incredible ability could bring to bear in a large-scale battle like this.

Besides…

*There’s one mage among them who’s especially skilled. Skilled enough to hold me and Old Master back with Magic.*

The principle was different, but Magic, too, was ultimately an ability drawn from qi.

That was why even a fairly advanced mage wouldn’t pose much of a threat to me or Jeok Cheongang.

Unless they were one of the rare few said to have reached the very edge of truth.

“……A Grand Mage.”

The title slipped from my lips like a groan.

And just as I was about to conclude that one of them had to be a Grand Mage, a question suddenly occurred to me.

*If they really have a Grand Mage, how has the situation stayed like this?*

I didn’t mean that we were winning.

Even though everyone, myself included, was giving it their all, the battle was clearly going badly for our side.

*But if the Grand Mage had stepped in, we wouldn’t even have been able to keep things at this disadvantage.*

I knew better than anyone the effect a Grand Mage could have on a battlefield. It didn’t take much thought.

A wide-area attack spell unlike anything the world had ever seen.

How long could an allied army, at least a third of which was made up of undisciplined rabble, last against that incomprehensible power—a natural disaster with a will of its own?

And yet the supposed Grand Mage hadn’t stepped in.

They’d used gravity magic to hinder Jeok Cheongang and me for a moment, and body-enhancement magic to help the Blood-Sword Demon Lord. But they hadn’t done anything beyond that.

Squish.

The Blood-Sword Demon Lord had crossed the blood-red path, and now, in this very moment, his steps finally came to a halt.

“What exactly… are you after?”

I was genuinely curious—and uneasy.

Were the mages holding back because they were preparing a powerful spell that could end the battle at once?

Or were they plotting some other scheme?

In response to my question, which I’d blurted out before I could stop myself, the Blood-Sword Demon Lord, watching us with a smile from three *jang* away, suddenly furrowed his brow.

“After? From the start, I’ve only been after two things in this battle: victory and you.”

“You sure took a long time to say you don’t want to answer.”

“I don’t know what you’re talking about, but… it doesn’t matter.”

The Blood-Sword Demon Lord shrugged with an expression that could have been sincere or an act, then raised the sword he’d been holding loosely and continued.

“Let’s finish this. Of course, I’d prefer an ending where one of you dies and the other is taken prisoner.”

Jeok Cheongang and I answered together, in one voice.

“Go fuck yourself.”

And at that moment—

PAPAT!

We charged at the Blood-Sword Demon Lord.

No—more precisely, only Jeok Cheongang shot toward him.

*Hold him off for half a quarter-hour. Just half a quarter-hour.*

With that Sound Transmission sent through the wind, I twisted my body and charged toward the hill.

SHWEEEE!
```
